from fastapi import APIRouter, Depends, HTTPException, Header, Path
from sqlalchemy.orm import Session
from app.database.conexion import get_db
from app.utils import build_message, verify_signature
from app.schemas.mediciones import MedicionRequest
import logging
import re

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/estaciones/{station_code}/mediciones")
async def recive_data(
    station_code: str = Path(...),
    data: MedicionRequest = ...,
    signature: str = Header(..., alias="Signature"),
    db: Session = Depends(get_db)
):  
    
    if not re.match(
        r"^[A-Z0-9_-]+$",
        station_code
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid station code"
        )

    print("station_code:", station_code, "\n")
    print("data:", data)
    print("\n")
    print("signature:", signature)

    ## Verficacion de firma encriptada para seguradad de la api
    # message = build_message(
    #     station_code.strip(),
    #     data
    # )
    # secret_key = # Obtener llave secreta de la estacion. station.secret_key

    
    # if not verify_signature(
    #     message,
    #     secret_key,
    #     signature
    # ):
    #     raise HTTPException(
    #         status_code=401,
    #         detail="Firma inválida"
    #     )
    
    # print("Firma Acceptada: ", signature)

    return {
        "status": "received",
        "station_id": station_code
    }