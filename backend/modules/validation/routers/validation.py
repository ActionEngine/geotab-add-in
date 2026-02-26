from fastapi import APIRouter, Depends

from modules.auth.dependencies.auth import get_current_user
from modules.validation.dependencies.validation import (
    get_segment_anomalies_impl,
    get_distance_to_road_with_location_impl,
    get_idle_outliers_impl,
    get_teleportation_validation_results_impl,
    get_validations_by_device_impl,
    get_validations_impl,
)
from modules.validation.schemas.validation import (
    DistanceToRoadWithLocationResponse,
    IdleOutlierResponse,
    SegmentAnomalyResponse,
    TeleportationValidationResultResponse,
    ValidationByDeviceResponse,
    ValidationResponse,
)

router = APIRouter(prefix="/validation", tags=["validation"])


@router.get("", response_model=list[ValidationResponse])
async def get_validations(
    current_user: dict = Depends(get_current_user),
) -> list[ValidationResponse]:
    return await get_validations_impl(current_user)


@router.get("/by-device", response_model=list[ValidationByDeviceResponse])
async def get_validations_by_device(
    current_user: dict = Depends(get_current_user),
) -> list[ValidationByDeviceResponse]:
    return await get_validations_by_device_impl(current_user)


@router.get(
    "/distance-to-road",
    response_model=list[DistanceToRoadWithLocationResponse],
)
async def get_distance_to_road_with_location(
    device_id: str | None = None,
    current_user: dict = Depends(get_current_user),
) -> list[DistanceToRoadWithLocationResponse]:
    return await get_distance_to_road_with_location_impl(current_user, device_id)


@router.get(
    "/teleportation", response_model=list[TeleportationValidationResultResponse]
)
async def get_teleportation_validation_results(
    device_id: str | None = None,
    current_user: dict = Depends(get_current_user),
) -> list[TeleportationValidationResultResponse]:

    return await get_teleportation_validation_results_impl(current_user, device_id)


@router.get("/idle-outliers", response_model=list[IdleOutlierResponse])
async def get_idle_outliers(
    device_id: str | None = None,
    current_user: dict = Depends(get_current_user),
) -> list[IdleOutlierResponse]:

    return await get_idle_outliers_impl(current_user, device_id)


@router.get("/segment_anomaly", response_model=list[SegmentAnomalyResponse])
async def get_segment_anomalies(
    device_id: str | None = None,
    current_user: dict = Depends(get_current_user),
) -> list[SegmentAnomalyResponse]:

    return await get_segment_anomalies_impl(current_user, device_id)
