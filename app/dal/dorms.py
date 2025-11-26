from sqlmodel import Session
from app.models.dorms import Dorm

class DormsDAL:
    def __init__(self, session: Session):
        self.session = session
        
    def add_dorm(self):
        dorm = Dorm()
        self.session.add(dorm)
        self.session.commit()
        self.session.refresh(dorm)