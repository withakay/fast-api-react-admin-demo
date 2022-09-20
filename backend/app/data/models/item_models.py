from decimal import Decimal
from typing import Optional

from sqlmodel import Field, SQLModel

from pydantic import BaseModel


class ItemBase(SQLModel):
    __tablename__ = "items"

    name: str = Field(unique=True, index=True, nullable=False)
    price: Decimal = Field(nullable=False)


class Item(ItemBase, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)


class ItemSummary(BaseModel):
    total: Decimal
