import os
from dotenv import load_dotenv

# Force reload the .env file
load_dotenv(override=True)

# Debug: Verify the API key is loaded
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    print(f"DEBUG: Key found in env: {api_key[:5]}...")
else:
    print("DEBUG: GOOGLE_API_KEY not found!")

import shutil
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from analysis import analyze_csv
from gemini_client import generate_report

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Ensure uploads folder exists
os.makedirs("uploads", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, file: UploadFile = File(...)):
    filepath = f"uploads/{file.filename}"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    data_summary = analyze_csv(filepath)
    report = generate_report(data_summary)

    os.remove(filepath)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "report": report,
            "filename": file.filename
        }
    )