import logging
import os

from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from modules.auth.dependencies.auth import get_current_user

# Import routers
from modules.geotab_database.routers.geotab_database import router as database_router
from modules.geotab_location.routers.mvt import router as mvt_router
from modules.validation.routers.validation import router as validation_router

logger = logging.getLogger(__name__)

load_dotenv()

default_allowed_origins = ["*"]

allowed_origins_env = os.getenv("ALLOWED_ORIGINS")
allowed_origins = (
    [origin.strip() for origin in allowed_origins_env.split(",") if origin.strip()]
    if allowed_origins_env
    else default_allowed_origins
)


app = FastAPI(title="Aspen Geotab Add-in Backend", version="0.0.1")

# Include routers
app.include_router(database_router)
app.include_router(mvt_router)
app.include_router(validation_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def private_network_access_middleware(request: Request, call_next):
    response = await call_next(request)

    if request.headers.get("access-control-request-private-network") == "true":
        response.headers["Access-Control-Allow-Private-Network"] = "true"

    return response


@app.get("/")
async def root(user=Depends(get_current_user)):
    return {
        "message": f"Hello, {user['email'] or user['id']}",
        "user_id": user["id"],
        "email": user["email"],
    }
