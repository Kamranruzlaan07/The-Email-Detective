from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.email import EmailHeaderRequest
from app.modules.report_builder import build_report


app = FastAPI(
    title="The Email Detective"
)


# CORS Configuration
# Allows local development and production Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://the-email-detective.vercel.app",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "The Email Detective API is running"
    }


@app.post("/analyze")
def analyze_email(request: EmailHeaderRequest):
    """
    Analyze raw email headers.
    """
    return build_report(request.header)


@app.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...)):
    """
    Analyze uploaded .eml files.
    """

    content = await file.read()

    try:
        email_text = content.decode("utf-8")
    except UnicodeDecodeError:
        email_text = content.decode("latin-1")

    return build_report(email_text)