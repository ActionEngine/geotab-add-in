from datetime import datetime

from pydantic import BaseModel


class ValidationResponse(BaseModel):
    id: int
    geotab_database_id: int | None
    started_at: datetime
    finished_at: datetime | None
    validation_type: str
    warnings: int
    errors: int
    total: int
    status: str


class ValidationByDeviceResponse(BaseModel):
    validation_id: int
    device_id: str
    total: int
    warnings: int
    errors: int


class DistanceToRoadWithLocationResponse(BaseModel):
    validation_id: int
    geotab_location_id: int
    distance: float
    datetime: datetime
    device_id: str
    external_id: str
    speed: int
    longitude: float | None
    latitude: float | None


class TeleportationValidationResultResponse(BaseModel):
    """Response model for teleportation validation results, including location details."""

    validation_id: int
    geotab_location_id: int
    implied_speed_kmh: float
    datetime: datetime
    device_id: str
    external_id: str
    longitude: float | None
    latitude: float | None


class IdleOutlierResponse(BaseModel):
    """Response model for idle outlier validation results, including location details."""

    validation_id: int
    geotab_location_id: int
    datetime: datetime
    device_id: str
    external_id: str
    longitude: float | None
    latitude: float | None


class SegmentAnomalyResponse(BaseModel):
    """Response model for segment anomaly detection results, including location details."""

    validation_id: int
    geotab_database_id: int
    segment_id: int
    diagnostic_ids: list[str]
    current_values: list[float]
    reference_values: list[float]
    value_deviations: list[float]
    aggregate_deviation: float
    is_warning: bool
    is_error: bool
    device_ids: list[str]
