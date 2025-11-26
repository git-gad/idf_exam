from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
import csv
from io import StringIO
from app.db.database import get_db
from app.models.soldiers import Soldier
from app.dal.soldiers import SoldiersDAL

router = APIRouter(prefix="", tags=["soldiers"])

def get_soldiers_dal(session: Session = Depends(get_db)) -> SoldiersDAL:
    return SoldiersDAL(session)

@router.get('/search/{private_num}')
def get_by_private_num(private_num: int, dal: SoldiersDAL = Depends(get_soldiers_dal)):
    soldier = dal.get_by_private_num(private_num)
    if not soldier:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return soldier

@router.get('/all')
def get_all(dal: SoldiersDAL = Depends(get_soldiers_dal)):
    return dal.get_all()