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
