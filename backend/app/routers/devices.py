from fastapi import APIRouter, HTTPException

from app.services.adb_service import (
    list_devices,
    get_connected_device
)

router = APIRouter(prefix="/api/devices", tags=["Devices"])

@router.get("")
def get_devices():
    try:
        devices = list_devices()

        return {
            "total": len(devices),
            "devices": devices
        }

    except RuntimeError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error)
        )
        
@router.get("/current")
def get_current_device():
    try:
        device = get_connected_device()

        return {
            "connected": True,
            "device": device
        }

    except RuntimeError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error)
        )