from pathlib import Path
import traceback
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="TripMate AI",
    description="LangGraph Multi-Agent Travel Planner with FastAPI Frontend",
    version="1.0.0"
)