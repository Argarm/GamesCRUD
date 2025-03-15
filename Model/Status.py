from enum import Enum


class Status(Enum):
    NOT_STARTED = "not started"
    NOW_PLAYING = "now playing"
    BEATEN = "beaten"
    COMPLETED = "completed"
    ABANDONED = "abandoned"
