import os

from fastapi import FastAPI

from models import Technology, Project, response

from utils.otp_auth import authenticate_otp, unauthorized_msg
from utils.mongodb import MongoDB
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
mongodb = MongoDB("ProjectTrackerAPI")


@app.get("/")
async def root():
    return {"message": "This is an API I built for managing all the projects that I build"}


@app.get("/technologies")
async def get_technologies(otp: str = None):
    """Returns a list of all technologies."""
    if os.getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    return response(
        True,
        "Successfully retrieved all technologies.",
        mongodb.find("technologies", {})
    )


@app.get("/technologies/{technology_id}")
async def get_technology(technology_id: int, otp: str = None):
    """Returns a single technology."""
    if os.getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    if technology := mongodb.find_one("technologies", {"_id": technology_id}):
        return response(True, "Successfully retrieved technology.", technology)
    else:
        return response(False, "Technology not found.")


@app.get("/projects")
async def get_projects(otp: str = None):
    """Returns a list of all projects."""
    if os.getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    return response(
        True,
        "Successfully retrieved all projects.",
        mongodb.find("projects", {})
    )


@app.get("/projects/{project_id}")
async def get_project(project_id: int, otp: str = None):
    """Returns a single project."""
    if os.getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    if project := mongodb.find_one("projects", {"_id": project_id}):
        return response(True, "Successfully retrieved project.", project)
    else:
        return response(False, "Project not found.")
