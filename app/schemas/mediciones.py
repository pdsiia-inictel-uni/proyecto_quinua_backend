from pydantic import BaseModel
from typing import Optional


class MedicionSensorRequest(BaseModel):
    sensor_id: str
    valor: float
    calidad: str


class EventRequest(BaseModel):
    tipo: str
    mensaje: str

class MedicionRequest(BaseModel):
    timestamp: int

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    nivel_bateria: Optional[float] = None

    mediciones: list[MedicionSensorRequest]

    eventos: Optional[
        list[EventRequest]
    ] = None
