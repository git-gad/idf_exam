from sqlmodel import Field, SQLModel
# from sqlalchemy import CheckConstraint

class Dorm(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    places: int = Field(default=80, nullable=False)



    