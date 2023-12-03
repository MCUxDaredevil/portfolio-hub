from pydantic import BaseModel
from typing import Optional
from enum import IntEnum


class Proficiency(IntEnum):
    Novice = 0.2
    Beginner = 0.4
    Intermediate = 0.6
    Advanced = 0.8
    Expert = 1.0


class Project(BaseModel):
    project_id: str
    name: str
    summary: str
    description: Optional[str]
    github_repo: Optional[str]
    live_url: Optional[str]
    tags: list[str] = []
    image: Optional[str]
    technologies: list[str] = []


class Technology(BaseModel):
    technology_id: str
    name: str
    description: Optional[str]
    proficiency: Proficiency = Proficiency.Novice
    image: Optional[str]
    projects: list[str] = []


