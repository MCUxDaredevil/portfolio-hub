import os

from fastapi import APIRouter

from models import response, Project
from utils.mongodb import MongoDB
from utils.otp_auth import authenticate_otp, unauthorized_msg

router = APIRouter()
mongodb = MongoDB("ProjectTrackerAPI")


@router.get("/projects")
async def get_projects(otp: str = None):
    """Returns a list of all projects."""
    if os.getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    return response(
        True,
        "Successfully retrieved all projects.",
        mongodb.find("projects", {})
    )


@router.get("/projects/{project_id}")
async def get_project(project_id: int, otp: str = None):
    """Returns a single project."""
    if os.getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    if project := mongodb.find_one("projects", {"_id": project_id}):
        return response(True, "Successfully retrieved project.", project)
    else:
        return response(False, "Project not found.")