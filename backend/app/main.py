from fastapi import FastAPI

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