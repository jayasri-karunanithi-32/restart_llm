from fastapi import FastAPI
from app.routes import file

app = FastAPI()

@app.get("/")
def landing_page():
    return{
        "message" : " welcome"
    }

@app.get("/health")
def health():
    return{
        "status":"ok"
    }
app.include_router(file.router)