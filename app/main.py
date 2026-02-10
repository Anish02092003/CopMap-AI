from fastapi import FastAPI
from app.cv.detect import analyze_frame
from app.alerts.rules import generate_alert

from app.db.database import engine, SessionLocal
from app.db.models import Base, PatrolLog
from app.rag.embed import add_document
from app.rag.summary import generate_summary
from fastapi import File, UploadFile
import shutil
import os
from app.alerts.suspicious import detect_suspicious


from pydantic import BaseModel
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


app = FastAPI(title="CopMap AI Patrol Intelligence")

class PatrolLogRequest(BaseModel):
    location: str
    text: str
    crowd_level: str


@app.get("/")
def home():
    return {"message": "CopMap AI system running"}

Base.metadata.create_all(bind=engine)


@app.post("/detect")
def detect(file: UploadFile = File(...), location: str = "Market Road"):
    os.makedirs("sample_data", exist_ok=True)

    file_path = f"sample_data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_frame(file_path)

    alerts = generate_alert(
        location,
        result["people_count"],
        result["crowd_density"]
    )

    suspicious = detect_suspicious(location, result["people_count"])

    return {
        "location": location,
        "analysis": result,
        "alerts": alerts,
        "suspicious_activity": suspicious
    }



@app.post("/patrol-log")
def add_patrol_log(data: PatrolLogRequest):
    db = SessionLocal()

    log = PatrolLog(
        location=data.location,
        text=data.text,
        crowd_level=data.crowd_level
    )

    db.add(log)
    db.commit()
    db.refresh(log)
    db.close()

    add_document(data.text)

    return {"message": "Patrol log stored", "id": log.id}

@app.get("/intelligence-summary")
def intelligence_summary(query: str = "crowd"):
    summary = generate_summary(query)
    return {"summary": summary}



