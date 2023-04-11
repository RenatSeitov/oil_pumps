from typing import Union

from pydantic import BaseModel


class Pumps(BaseModel):
    id: int
    pressure: Union[int, None]
    temperature: Union[int, None]
    speed: Union[int, None]
