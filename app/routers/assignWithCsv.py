from fastapi import APIRouter, UploadFile, File, Depends
from sqlmodel import Session
import csv
from io import StringIO
from app.db.database import get_db
from app.dal.soldiers import SoldiersDAL

router = APIRouter(prefix="", tags=["soldiers"])

def get_soldiers_dal(session: Session = Depends(get_db)) -> SoldiersDAL:
    return SoldiersDAL(session)

@router.post("/")
def assign_soldiers(file: UploadFile = File(...), dal: SoldiersDAL = Depends(get_soldiers_dal)):
    content = file.file.read().decode('utf-8')
    reader = csv.reader(StringIO(content))
    reader = csv.DictReader(StringIO(content))
    dal.add_soldiers(reader)
    result = dal.assign_to_dorms()
    return result
    
   