import os
import shutil
from fastapi import FastAPI, HTTPException, File, Form, UploadFile, BackgroundTasks
from pydantic import BaseModel, EmailStr
from typing import Optional
from dotenv import load_dotenv
from app.db import Patient, engine, SessionLocal, Base
load_dotenv()
app = FastAPI()



@app.get("/")
def read_root():
    return {"message": "API is working OK"}


# model for patient
class PatientRegistration(BaseModel):
    name: str
    email: EmailStr
    phone: str

# endpoint for patient registration
@app.post("/register")
async def register_patient(
    name: str = Form(...),
    email: EmailStr = Form(...),
    phone: str = Form(...),
    document_photo: UploadFile = File(...),
    background_tasks: BackgroundTasks = BackgroundTasks()
):
    try:
        log_request(name, email, phone, document_photo.filename)
        # input validation
        patient_data = PatientRegistration(name=name, email=email, phone=phone)

        # photo file save
        photo_path = f"uploads/{document_photo.filename}"
        with open(photo_path, "wb") as buffer:
            shutil.copyfileobj(document_photo.file, buffer)

        # save database
        db = SessionLocal()
        patient = Patient(
            name=patient_data.name,
            email=patient_data.email,
            phone=patient_data.phone,
            document_photo=photo_path,
        )
        db.add(patient)
        db.commit()
        db.refresh(patient)
        db.close()
        # send email async
        return {"message": "Patient successfully registered"}
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=422, detail=str(e))


def log_request(name, email, phone, file):
    print(f"Received data: name={name}, email={email}, phone={phone}, file={file}")
