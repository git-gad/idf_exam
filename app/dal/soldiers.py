from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError
from app.models.soldiers import Soldier
from app.models.dorms import Dorm

class SoldiersDAL:
    def __init__(self, session: Session):
        self.session = session
        
    def add_soldiers(self, csv_reader):
        soldiers = list(csv_reader)
        sorted_soldiers = sorted(soldiers, key=lambda d: d['מרחק מהבסיס'], reverse=True)
        for row in sorted_soldiers:
            soldier = Soldier(private_num=row['מספר אישי'],
                            first_name=row['שם פרטי'],
                            last_name=row['שם משפחה'],
                            gender=row['מין'],
                            city=row['עיר מגורים'],
                            distance=row['מרחק מהבסיס'])
            try:
                self.session.add(soldier)
                self.session.commit()
                self.session.refresh(soldier)
            except IntegrityError:
                self.session.rollback()
                return None
        
            
    def get_all(self) -> list[Soldier]:
        return self.session.exec(select(Soldier)).all()    
    
    def assign_to_dorms(self):
        soldiers = self.get_all()
        total = len(soldiers)
        placed = 0
        for i in range(80):
            soldiers[i].placed_in_dorm = True
            placed += 1
        for i in range(80, 161):
            soldiers[i].placed_in_dorm = True
            placed += 1
        not_placed = total - placed
        return {'placed': placed, 'not_placed': not_placed}

            