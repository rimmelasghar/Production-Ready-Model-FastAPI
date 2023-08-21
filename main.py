from fastapi import FastAPI
from app.main import app as fastapi_app

app = FastAPI()

# Mounted the FastAPI app from the "app" folder as a sub-application
app.mount("/app", fastapi_app)
