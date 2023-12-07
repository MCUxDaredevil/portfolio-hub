import os

from fastapi import FastAPI
from pymongo import MongoClient

from models import Technology, Project, response

from utils.otp_auth import authenticate_otp
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
        return response(False, "You are not authorized to access this route.")
    return response(
        True,
        "Successfully retrieved all technologies.",
        mongodb.find("technologies", {})
    )

