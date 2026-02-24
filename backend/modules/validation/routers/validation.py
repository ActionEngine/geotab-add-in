from fastapi import APIRouter, Depends

from modules.auth.dependencies.auth import get_current_user
from modules.validation.dependencies.validation import (
    get_validations_by_device_impl,
    get_validations_impl,
)
from modules.validation.schemas.validation import (
    ValidationByDeviceResponse,
    ValidationResponse,
)

router = APIRouter(prefix="/validation", tags=["validation"])


@router.get("", response_model=list[ValidationResponse])
async def get_validations(
    current_user: dict = Depends(get_current_user),
) -> list[ValidationResponse]:
    return await get_validations_impl(current_user)


@router.get("/by-device", response_model=list[ValidationByDeviceResponse])
async def get_validations_by_device(
    current_user: dict = Depends(get_current_user),
) -> list[ValidationByDeviceResponse]:
    return await get_validations_by_device_impl(current_user)
