import logging
from fastapi import FastAPI, Depends

from modules.auth.dependencies.auth import get_current_user
from modules.geotab_database.routers.geotab_database import router as database_router

logger = logging.getLogger(__name__)


app = FastAPI(title="Aspen Geotab Add-in Backend", version="0.0.1")

# Include routers
app.include_router(database_router)


@app.get("/")
async def root(user = Depends(get_current_user)):
    return {
        "message": f"Hello, {user['email'] or user['id']}",
        "user_id": user['id'],
        "email": user['email'],
    }
