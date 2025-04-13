from db.models import Base
from db.session import engine

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.answers import router as answer_router
from db.session import get_db
from sqlalchemy.orm import Session
from routes.upload_db import router as upload_db_router
from fastapi import Depends
from auth.routes import auth_router
from routes.users import router as me_router
from fastapi.staticfiles import StaticFiles
from pathlib import Path

load_dotenv()

Base.metadata.create_all(bind=engine)  # Temporary until you use Alembic

app = FastAPI()
from pathlib import Path
from fastapi.staticfiles import StaticFiles

# Absolute path to the frontend build directory
frontend_path = Path(__file__).resolve().parent.parent / "frontend" / "build"
if not frontend_path.exists():
    print(f"❌ Could not find frontend build folder at: {frontend_path}")
else:
    print(f"✅ Found frontend build folder at: {frontend_path}")

app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(answer_router, prefix="/answers", tags=["Answers"])
app.include_router(upload_db_router, prefix="/upload-db", tags=["Upload & Store"])
app.include_router(me_router, prefix="/user", tags=["Dashboard"])


@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "QuizGen FastAPI backend is running!"}
from fastapi.routing import APIRoute

def list_routes(app):
    routes = []
    for route in app.routes:
        if isinstance(route, APIRoute):
            routes.append({
                "path": route.path,
                "name": route.name,
                "methods": route.methods
            })
    return routes

# Print all registered routes
for r in list_routes(app):
    print(f"{r['methods']} -> {r['path']} (name: {r['name']})")
