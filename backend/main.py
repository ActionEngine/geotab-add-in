import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from alembic import command
from alembic.config import Config

from modules.auth.routers import auth
from modules.auth.dependencies import get_current_user
from modules.auth.models.user import User

logger = logging.getLogger(__name__)


def run_migrations():
    """Run Alembic migrations"""

    logger.info("Running database migrations...")
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    logger.info("✓ Migrations applied")


@asynccontextmanager
async def lifespan(app: FastAPI):
    run_migrations()

    yield

    logger.info("Shutting down...")


app = FastAPI(title="Geotab Add-in Backend", version="0.0.1", lifespan=lifespan)
app.include_router(auth.router)


@app.get("/")
async def root(user: User = Depends(get_current_user)):
    return {
        "message": f"Hello, {user.email or user.geotab_id}",
        "user_id": user.geotab_id,
        "email": user.email,
    }
