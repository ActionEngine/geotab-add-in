import logging
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from modules.auth.dependencies.auth import get_current_user

# Import routers
from modules.geotab_database.routers.geotab_database import router as database_router
from modules.geotab_location.routers.mvt import router as mvt_router
from modules.validation.routers.validation import router as validation_router

logger = logging.getLogger(__name__)


app = FastAPI(title="Aspen Geotab Add-in Backend", version="0.0.1")

# Include routers
app.include_router(database_router)
app.include_router(mvt_router)
app.include_router(validation_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root(user=Depends(get_current_user)):
    return {
        "message": f"Hello, {user['email'] or user['id']}",
        "user_id": user["id"],
        "email": user["email"],
    }
