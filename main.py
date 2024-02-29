from os import getenv

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette import status

from models import response, Project
from utils.json_handler import get_user
from utils.mongodb import MongoDB
from utils.otp_auth import unauthorized_msg, authenticate_otp

load_dotenv()
app = FastAPI()

mongodb = MongoDB("ProjectTrackerAPI")


@app.get("/")
async def root():
    """Redirects to the API documentation."""
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


@app.get("/projects")
async def get_projects(otp: str = None):
    """Returns a list of all projects."""
    if getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    if getenv("LOCAL") == "True":
        data = mongodb.find("admin", {"_id": "projects"})
    elif user := get_user():
        data = mongodb.find(user, {"_id": "projects"})
    else:
        return response(False, "User not found.")

    return response(True, "Successfully retrieved all projects.", data)


@app.get("/projects/{project_id}")
async def get_project(project_id: int, otp: str = None):
    """Returns a single project."""
    if getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    if project := mongodb.find_one("projects", {"_id": project_id}):
        return response(True, "Successfully retrieved project.", project)
    else:
        return response(False, "Project not found.")


@app.post("/projects/add")
async def add_project(project: Project, otp: str = None):
    """Adds a new project."""
    if getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    if mongodb.insert_one("projects", project.model_dump()):
        return response(True, "Successfully added project.", project.dict())
    else:
        return response(False, "Failed to add project.")


@app.get("/technologies")
async def get_technologies(otp: str = None):
    """Returns a list of all technologies."""
    if getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    return response(
        True,
        "Successfully retrieved all technologies.",
        mongodb.find("technologies", {})
    )


@app.get("/technologies/{technology_id}")
async def get_technology(technology_id: int, otp: str = None):
    """Returns a single technology."""
    if getenv("AUTH") != "False" and not authenticate_otp(otp):
        return response(**unauthorized_msg)

    if technology := mongodb.find_one("technologies", {"_id": technology_id}):
        return response(True, "Successfully retrieved technology.", technology)
    else:
        return response(False, "Technology not found.")
