from fastapi import FastAPI, UploadFile, File, Depends
from io import StringIO
from app.db.database import init_db
from app.routers import assignWithCsv
from app.dal.soldiers import SoldiersDAL
from sqlmodel import Session
from app.db.database import get_db
from app.dal.dorms import DormsDAL
import csv

app = FastAPI()

init_db()

# def get_dorms_dal(session: Session = Depends(get_db)) -> DormsDAL:
#     return DormsDAL(session)

# dorm_dal = get_dorms_dal()
# dorm_dal.add_dorm()
# dorm_dal.add_dorm()

def get_soldiers_dal(session: Session = Depends(get_db)) -> SoldiersDAL:
    return SoldiersDAL(session)
# app.include_router(assignWithCsv.router, prefix="/assignWithCsv", tags=["Soldiers"])

@app.post("/assignWithCsv")
def assign_soldiers(file: UploadFile, dal: SoldiersDAL = Depends(get_soldiers_dal)):
    content = file.file.read().decode('utf-8')
    reader = csv.DictReader(StringIO(content))
    dal.add_soldiers(reader)
    rows = list(reader)
    result = dal.assign_to_dorms()
    return result
    # return {'ok':'ok'}
    # reader = csv.reader(StringIO(content))
    # header = next(reader)
    


