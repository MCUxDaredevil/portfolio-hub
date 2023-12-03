from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Depends
from models import Technology, Project
from typing import Annotated

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def root():
    return {"message": "This is an API I built for managing all the projects that I build"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
