from fastapi import HTTPException, status

import app.data.models as models

from sqlalchemy.orm import Session
from sqlalchemy.sql import functions as func


def get_item(db: Session, id: int):
    if item := db.query(models.Item).filter_by(id=id).first():
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")


def get_items(
    db: Session, skip: int = 0, limit: int = 100
) -> list[models.Item]:
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_items_summary(db: Session) -> models.ItemSummary:
    return models.ItemSummary(
        total=db.query(func.sum(models.Item.price)).scalar()
    )


def create_item(db: Session, item: models.Item):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def edit_item(db: Session, item_id, item: models.Item):
    db_item = get_item(db, item_id)
    update_data = item.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, id: int) -> None:
    item = get_item(db, id)
    db.delete(item)
    db.commit()
