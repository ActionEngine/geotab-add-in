from pydantic import BaseModel, Field


class GeotabAuthRequest(BaseModel):
    """Request model for Geotab token authentication"""

    geotab_token: str = Field(
        ...,
        description="OAuth2 token Geotab",
    )


class GeotabCredentialsRequest(BaseModel):
    """Request model for Geotab username/password authentication"""

    username: str = Field(
        ...,
        description="Email or username in Geotab system",
        min_length=3,
    )
    password: str = Field(
        ...,
        description="Password for Geotab account",
        min_length=1,
    )
    database: str = Field(
        ...,
        description="Full Geotab database URL in format: https://my.geotab.com/database_name",
        min_length=10,
    )

    class Config:
        json_schema_extra = {
            "example": {
                "username": "user@example.com",
                "password": "your_password",
                "database": "https://my.geotab.com/demo_geobase",
            }
        }


class TokenResponse(BaseModel):
    """Response model for authentication endpoints"""

    access_token: str = Field(
        ...,
        description="JWT token for authorization",
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    )
    user_id: str = Field(..., description="Geotab user ID", example="b1234")
    email: str | None = Field(
        None, description="User email", example="user@example.com"
    )
