from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from app.api.v1.endpoints import router as analyze_router

app = FastAPI(title="The Repository Oracle")

# Include the API router
app.include_router(analyze_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to The Repository Oracle API"}
