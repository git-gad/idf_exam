from sqlmodel import Field, SQLModel, String, Column
from sqlalchemy import CheckConstraint

class Soldier(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    private_num: int 
    first_name: str 
    last_name: str 
    gender: str
    city: str 
    distance: int 
    placed_in_dorm: bool | None = Field(default=False)
    
    # __table_args__ = (
    #     CheckConstraint('private_num >= 8000000', name='check_private_num_positive'),
    # )
    
        


