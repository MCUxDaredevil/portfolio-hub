from pydantic import BaseModel
from typing import Optional, Any
from enum import IntEnum, Enum


class Tags(Enum):
    projects = ["projects"]
    technologies = ["technologies"]


class Proficiency(IntEnum):
    Novice = 0.2
    Beginner = 0.4
    Intermediate = 0.6
    Advanced = 0.8
    Expert = 0.99  # Can never be 1.0


class Project(BaseModel):
    _id: int
    name: str
    summary: str
    description: Optional[str]
    github_repo: Optional[str]
    live_url: Optional[str]
    tags: list[str] = []
    image: Optional[str]
    technologies: list[dict[int, str]] = []


class Technology(BaseModel):
    _id: int
    name: str
    description: Optional[str]
    proficiency: Proficiency = Proficiency.Novice
    image: Optional[str]
    projects: list[dict[int, str]] = []


def response(success: bool, message: str, data: Any = None) -> dict:
    """Returns a formatted response."""
    return {
        "success": success,
        "message": message,
        "data": data
    }
