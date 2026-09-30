import hmac
import hashlib
from decimal import Decimal
from app.schemas.mediciones import MedicionRequest

ONLINE_TIMEOUT = 24 * 60 * 60

def normalize_empty(value):
    """
    Normaliza valores Na o nulos y deciemales a precision de 2 decimales
    """
    if value is None:
        return "NA"

    s = format(Decimal(str(value)), "f").rstrip("0")

    if s.endswith("."):
        s += "0"

    return s


def build_message(
    station_code: str,
    data: MedicionRequest
) -> str:
    """
    Consutruye el mesaje para generacion de la firma hash encriptda
    """
    parts = [

        station_code,

        str(data.timestamp),
        normalize_empty(data.battery_level)

    ]

    for measurement in data.measurements:

        parts.append(
            measurement.sensor_code
        )

        parts.append(
            str(normalize_empty(measurement.value))
        )

    return "|".join(parts).strip()


def verify_signature(
    message: str,
    secret_key: str,
    received_signature: str
) -> bool:
    """
    Verifica si la firma encriptada generada en el servidor corresponde con la firma enviado por el api.
    """
    expected_signature = hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    print("expected_signature:", expected_signature)
    return hmac.compare_digest(
        expected_signature,
        received_signature
    )

def to_float(value):

    if value is None:
        return None

    return float(value)
