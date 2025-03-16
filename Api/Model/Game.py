from pydantic import BaseModel

from Api.Model.Format import Format
from Api.Model.PlatformChoice import PlatformChoice
from Api.Model.Status import Status

class Game(BaseModel):
    name: str
    developer: str
    release_date: str
    completed: bool = False
    format: Format
    my_time: int = 0
    platform: PlatformChoice
    status: Status
