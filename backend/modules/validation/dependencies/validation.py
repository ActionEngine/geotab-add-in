from sqlalchemy import select

from database.database import SessionLocal
from modules.geotab_database.services.geotab_database import get_database_by_email_and_name
from modules.validation.models.validation import Validation
from modules.validation.schemas.validation import ValidationResponse


async def get_validations_impl(current_user: dict) -> list[ValidationResponse]:
    email = current_user["email"]
    database_name = current_user["database"]
    db_entry = await get_database_by_email_and_name(email, database_name)

    if not db_entry:
        return []

    async with SessionLocal() as session:
        result = await session.execute(
            select(Validation)
            .where(Validation.geotab_database_id == db_entry.id)
            .order_by(Validation.started_at.desc())
        )
        validations = result.scalars().all()

    return [
        ValidationResponse(
            id=validation.id,
            geotab_database_id=validation.geotab_database_id,
            started_at=validation.started_at,
            finished_at=validation.finished_at,
            validation_type=validation.validation_type,
            warnings=validation.warnings,
            errors=validation.errors,
            total=validation.total,
            status=validation.status.value,
        )
        for validation in validations
    ]
