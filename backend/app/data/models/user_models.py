from typing import Optional
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True, nullable=False)
    first_name: Optional[str]
    last_name: Optional[str]
    is_active: bool = True
    is_superuser: bool = False


class User(UserBase, table=True):
    """
    User model
    This is a so called 'table' model, generally this should not
    be used directly via the API.
    """
    __tablename__ = "user"

    id: Optional[int] = Field(primary_key=True, index=True)
    hashed_password: Optional[str]


class UserOut(UserBase):
    id: Optional[int] = Field(primary_key=True, index=True)


class UserCreate(UserBase):
    password: str


class UserEdit(UserBase):
    password: Optional[str] = None




