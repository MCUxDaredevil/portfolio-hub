from fastapi import FastAPI
from dotenv import load_dotenv

from routes import projects, technologies

load_dotenv()
app = FastAPI()

app.include_router(projects.router)
app.include_router(technologies.router)


@app.get("/")
async def root():
    return {"message": "This is an API I built for managing all the projects that I build"}