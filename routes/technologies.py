import os

from fastapi import APIRouter

from models import response, Technology
from utils.mongodb import MongoDB
from utils.otp_auth import authenticate_otp, unauthorized_msg

router = APIRouter()
mongodb = MongoDB("ProjectTrackerAPI")


@router.get("/technologies")
async def get_technologies(otp: str = None):
    """Returns a list of all technologies."""
    if os.getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    return response(
        True,
        "Successfully retrieved all technologies.",
        mongodb.find("technologies", {})
    )


@router.get("/technologies/{technology_id}")
async def get_technology(technology_id: int, otp: str = None):
    """Returns a single technology."""
    if os.getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    if technology := mongodb.find_one("technologies", {"_id": technology_id}):
        return response(True, "Successfully retrieved technology.", technology)
    else:
        return response(False, "Technology not found.")