from fastapi import APIRouter, UploadFile, File, Depends
from sqlmodel import Session
import csv
from io import StringIO
from db import get_db

router = APIRouter()

@router.post("/upload_soldiers/")
def upload_agents(file: UploadFile = File(...), session: Session = Depends(get_db)):
    content = file.file.read().decode('utf-8')
    reader = csv.DictReader(StringIO(content))

    # created = []
    # for row in reader:
    #     agent = Agent(
    #         name=row["name"],
    #         clearance=int(row["clearance"]),
    #         email=row["email"]
    #     )
    #     session.add(agent)
    #     created.append(agent)

    # session.commit()
    # return {"created": len(created)}