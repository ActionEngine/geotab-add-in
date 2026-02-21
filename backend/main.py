import logging
from fastapi import FastAPI, Depends

from modules.auth.routers import auth
from modules.auth.dependencies import get_current_user
from modules.auth.models.user import User

logger = logging.getLogger(__name__)


app = FastAPI(title="Aspen Geotab Add-in Backend", version="0.0.1")
app.include_router(auth.router)


@app.get("/")
async def root(user: User = Depends(get_current_user)):
    return {
        "message": f"Hello, {user.email or user.geotab_id}",
        "user_id": user.geotab_id,
        "email": user.email,
    }
