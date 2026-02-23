from pydantic import BaseModel, Field, ConfigDict


class InitDatabaseRequest(BaseModel):
    user_name: str = Field(..., description="Geotab username/email")
    password: str = Field(..., description="Geotab password")
    database_name: str = Field(..., description="Geotab database name")


class InitDatabaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    database_name: str
    ingestion_status: str


class DatabaseEntryResponse(BaseModel):
    """Represents a Geotab database configuration entry for a user."""

    email: str
    database_name: str
    ingestion_status: str
    last_sync: str | None

    model_config = ConfigDict(from_attributes=True)


class DatabaseDetailsResponse(BaseModel):
    """Detailed information about a Geotab database configuration."""

    email: str
    database_name: str
    ingestion_status: str
    last_sync: str | None
    device_count: int
    location_rows: int
    status_data_rows: int
    actual_last_sync: str | None

    model_config = ConfigDict(from_attributes=True)
