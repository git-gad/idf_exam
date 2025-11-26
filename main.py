from fastapi import FastAPI, UploadFile, File, Depends
from io import StringIO
from app.db.database import init_db
from app.routers import assignWithCsv, soldiers
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

app.include_router(assignWithCsv.router, prefix="/assignWithCsv", tags=["soldiers"])
    
app.include_router(soldiers.router, prefix='/soldiers', tags=['soldiers'])
    


