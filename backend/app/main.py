from fastapi import FastAPI
from app.schemas.email import EmailHeaderRequest
from app.modules.report_builder import build_report

app = FastAPI(
    title="The Email Detective",
    version="0.1.0",
    description="An Email Investigation Platform"
)

@app.get("/")
def home():
    return {
        "application": "The Email Detective",
        "version": "0.1.0",
        "status": "Running 🚀"
    }

@app.post("/analyze")
def analyze_email(request: EmailHeaderRequest):
    return build_report(request.header)