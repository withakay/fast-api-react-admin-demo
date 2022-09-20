#!/usr/bin/env python3

from app.data.repositories.user_repository import create_user
from app.data.models import Item, UserCreate
from app.data.session import SessionLocal
from app.data.repositories.item_repository import create_item

def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="admin@brit-takehome-task.com",
            password="brit",
            is_active=True,
            is_superuser=True,
        ),
    )

    create_item(db, Item(name="Foo", price=100.00))
    create_item(db, Item(name="Bar", price=200.00))
    create_item(db, Item(name="Baz", price=349.99))
    create_item(db, Item(name="Quz", price=500.50))


if __name__ == "__main__":
    print("Creating superuser admin@brit-takehome-task.com")
    init()
    print("Superuser created")
