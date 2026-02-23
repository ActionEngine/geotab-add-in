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
    stats: dict

    model_config = ConfigDict(from_attributes=True)
