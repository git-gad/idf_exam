from sqlmodel import Field, SQLModel
# from sqlalchemy import CheckConstraint

class Dorm(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    places: int = Field(default=80, nullable=False)


# id: int | None = Field(default=None, primary_key=True)
#     private_num: int = Field(sa_column=Column(unique=True, nullable=False))
#     first_name: str = Field(sa_column=Column(String(20), nullable=False))
#     last_name: str = Field(sa_column=Column(String(20), nullable=False))
#     city: str = Field(sa_column=Column(String(20), nullable=False))
#     distance: int = Field(sa_column=Column(nullable=False))
#     placed_in_dorm: bool | None = Field(default=None)
    
#     __table_args__ = (
#         CheckConstraint('private_num >= 8000000', name='check_private_num_positive'),
#     )
    