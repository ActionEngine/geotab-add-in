import enum


class ValidationStatus(str, enum.Enum):
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
