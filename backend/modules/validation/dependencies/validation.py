from sqlalchemy import func, select

from modules.validation.models.segment_anomaly import SegmentAnomaly
from modules.validation.models.idle_outlier_result import IdleOutlierResult
from database.database import SessionLocal
from modules.geotab_database.services.geotab_database import (
    get_database_by_email_and_name,
)
from modules.geotab_location.models.geotab_location import GeotabLocation
from modules.validation.models.distance_to_road_result import DistanceToRoadResult
from modules.validation.models.validation_results_by_device import (
    DistanceToRoadByDevice,
)
from modules.validation.models.teleportation_result import TeleportationResult
from modules.validation.models.validation import Validation
from modules.validation.schemas.validation import (
    DistanceToRoadWithLocationResponse,
    IdleOutlierResponse,
    SegmentAnomalyResponse,
    TeleportationValidationResultResponse,
    ValidationByDeviceResponse,
    ValidationResponse,
)


async def get_validations_impl(current_user: dict) -> list[ValidationResponse]:
    email = current_user["email"]
    database_name = current_user["database"]
    db_entry = await get_database_by_email_and_name(email, database_name)

    if not db_entry:
        return []

    async with SessionLocal() as session:
        result = await session.execute(
            select(Validation)
            .where(Validation.geotab_database_id == db_entry.id)
            .order_by(Validation.started_at.desc())
        )
        validations = result.scalars().all()

    return [
        ValidationResponse(
            id=validation.id,
            geotab_database_id=validation.geotab_database_id,
            started_at=validation.started_at,
            finished_at=validation.finished_at,
            validation_type=validation.validation_type,
            warnings=validation.warnings,
            errors=validation.errors,
            total=validation.total,
            status=validation.status.value,
        )
        for validation in validations
    ]


async def get_validations_by_device_impl(
    current_user: dict,
) -> list[ValidationByDeviceResponse]:
    email = current_user["email"]
    database_name = current_user["database"]
    db_entry = await get_database_by_email_and_name(email, database_name)

    if not db_entry:
        return []

    async with SessionLocal() as session:
        result = await session.execute(
            select(DistanceToRoadByDevice)
            .join(Validation, Validation.id == DistanceToRoadByDevice.validation_id)
            .where(Validation.geotab_database_id == db_entry.id)
            .order_by(
                DistanceToRoadByDevice.validation_id.desc(),
                DistanceToRoadByDevice.device_id,
            )
        )
        rows = result.scalars().all()

    return [
        ValidationByDeviceResponse(
            validation_id=row.validation_id,
            device_id=row.device_id,
            total=row.total,
            warnings=row.warnings,
            errors=row.errors,
        )
        for row in rows
    ]


async def get_distance_to_road_with_location_impl(
    current_user: dict,
    device_id: str | None = None,
) -> list[DistanceToRoadWithLocationResponse]:
    email = current_user["email"]
    database_name = current_user["database"]
    db_entry = await get_database_by_email_and_name(email, database_name)

    if not db_entry:
        return []

    stmt = (
        select(
            DistanceToRoadResult.validation_id,
            DistanceToRoadResult.geotab_location_id,
            DistanceToRoadResult.distance,
            GeotabLocation.datetime,
            GeotabLocation.device_id,
            GeotabLocation.external_id,
            GeotabLocation.speed,
            func.ST_X(GeotabLocation.geometry).label("longitude"),
            func.ST_Y(GeotabLocation.geometry).label("latitude"),
        )
        .join(
            GeotabLocation,
            GeotabLocation.id == DistanceToRoadResult.geotab_location_id,
        )
        .join(Validation, Validation.id == DistanceToRoadResult.validation_id)
        .where(Validation.geotab_database_id == db_entry.id)
    )

    if device_id:
        stmt = stmt.where(GeotabLocation.device_id == device_id)

    stmt = stmt.order_by(
        DistanceToRoadResult.validation_id.desc(),
        GeotabLocation.datetime.desc(),
    )

    async with SessionLocal() as session:
        result = await session.execute(stmt)
        rows = result.all()

    return [
        DistanceToRoadWithLocationResponse(
            validation_id=row.validation_id,
            geotab_location_id=row.geotab_location_id,
            distance=row.distance,
            datetime=row.datetime,
            device_id=row.device_id,
            external_id=row.external_id,
            speed=row.speed,
            longitude=row.longitude,
            latitude=row.latitude,
        )
        for row in rows
    ]


async def get_teleportation_validation_results_impl(
    current_user: dict,
    device_id: str | None = None,
) -> list[TeleportationValidationResultResponse]:
    """Retrieve teleportation validation results for the authenticated user's database, optionally filtered by device ID."""

    email = current_user["email"]
    database_name = current_user["database"]
    db_entry = await get_database_by_email_and_name(email, database_name)

    if not db_entry:
        return []

    stmt = (
        select(
            TeleportationResult.validation_id,
            TeleportationResult.geotab_location_id,
            TeleportationResult.implied_speed_kmh,
            GeotabLocation.datetime,
            GeotabLocation.device_id,
            GeotabLocation.external_id,
            func.ST_X(GeotabLocation.geometry).label("longitude"),
            func.ST_Y(GeotabLocation.geometry).label("latitude"),
        )
        .join(
            GeotabLocation,
            GeotabLocation.id == TeleportationResult.geotab_location_id,
        )
        .join(Validation, Validation.id == TeleportationResult.validation_id)
        .where(Validation.geotab_database_id == db_entry.id)
    )

    if device_id:
        stmt = stmt.where(GeotabLocation.device_id == device_id)

    stmt = stmt.order_by(
        TeleportationResult.validation_id.desc(),
        GeotabLocation.datetime.desc(),
    )

    async with SessionLocal() as session:
        result = await session.execute(stmt)
        rows = result.all()

    return [
        TeleportationValidationResultResponse(
            validation_id=row.validation_id,
            geotab_location_id=row.geotab_location_id,
            implied_speed_kmh=row.implied_speed_kmh,
            datetime=row.datetime,
            device_id=row.device_id,
            external_id=row.external_id,
            longitude=row.longitude,
            latitude=row.latitude,
        )
        for row in rows
    ]


async def get_idle_outliers_impl(
    current_user: dict,
    device_id: str | None = None,
) -> list[IdleOutlierResponse]:
    """Retrieve idle outlier validation results for the authenticated user's database, optionally filtered by device ID."""

    email, database_name = current_user["email"], current_user["database"]
    db_entry = await get_database_by_email_and_name(email, database_name)

    if not db_entry:
        return []

    stmt = (
        select(
            GeotabLocation.id.label("geotab_location_id"),
            Validation.id.label("validation_id"),
            GeotabLocation.datetime,
            GeotabLocation.device_id,
            GeotabLocation.external_id,
            func.ST_X(GeotabLocation.geometry).label("longitude"),
            func.ST_Y(GeotabLocation.geometry).label("latitude"),
            IdleOutlierResult.is_outlier,
        )
        .join(
            IdleOutlierResult,
            IdleOutlierResult.geotab_location_id == GeotabLocation.id,
        )
        .join(Validation, Validation.id == IdleOutlierResult.validation_id)
        .where(Validation.geotab_database_id == db_entry.id)
    )

    if device_id:
        stmt = stmt.where(GeotabLocation.device_id == device_id)

    stmt = stmt.order_by(
        IdleOutlierResult.validation_id.desc(),
        GeotabLocation.datetime.desc(),
    )

    async with SessionLocal() as session:
        result = await session.execute(stmt)
        rows = result.all()

    return [
        IdleOutlierResponse(
            validation_id=row.validation_id,
            geotab_location_id=row.geotab_location_id,
            datetime=row.datetime,
            device_id=row.device_id,
            external_id=row.external_id,
            longitude=row.longitude,
            latitude=row.latitude,
            is_outlier=row.is_outlier,
        )
        for row in rows
    ]


async def get_segment_anomalies_impl(
    current_user: dict,
    device_id: str | None = None,
) -> list[SegmentAnomalyResponse]:
    """Retrieve segment anomaly detection results for the specified device in the authenticated user's database."""

    email, database_name = current_user["email"], current_user["database"]
    db_entry = await get_database_by_email_and_name(email, database_name)

    if not db_entry:
        return []

    stmt = select(SegmentAnomaly).where(SegmentAnomaly.geotab_database_id == db_entry.id)

    if device_id:
        stmt = stmt.where(SegmentAnomaly.device_ids.contains([device_id]))

    async with SessionLocal() as session:
        result = await session.execute(stmt)
        rows: list[SegmentAnomaly] = result.scalars().all()

    return [
        SegmentAnomalyResponse(
            validation_id=row.validation_id,
            geotab_database_id=row.geotab_database_id,
            segment_id=row.segment_id,
            diagnostic_ids=row.diagnostic_ids,
            current_values=row.current_values,
            reference_values=row.reference_values,
            value_deviations=row.value_deviations,
            aggregate_deviation=row.aggregate_deviation,
            is_warning=row.is_warning,
            is_error=row.is_error,
            device_ids=row.device_ids,
        )
        for row in rows
    ]
