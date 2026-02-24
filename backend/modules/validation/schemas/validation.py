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
