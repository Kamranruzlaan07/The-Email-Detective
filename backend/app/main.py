from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.email import EmailHeaderRequest
from app.modules.report_builder import build_report

app = FastAPI(title="The Email Detective")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze")
def analyze_email(request: EmailHeaderRequest):
    return build_report(request.header)


@app.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...)):
    content = await file.read()

    try:
        email_text = content.decode("utf-8")
    except UnicodeDecodeError:
        email_text = content.decode("latin-1")

    return build_report(email_text)