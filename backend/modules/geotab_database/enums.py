import enum


class IngestionStatus(str, enum.Enum):
    NONE = "NONE"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
