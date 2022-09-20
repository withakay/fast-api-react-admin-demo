#!/usr/bin/env python3

from app.data.repositories.user_repository import create_user
from app.data.models import UserCreate
from app.data.session import SessionLocal


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


if __name__ == "__main__":
    print("Creating superuser admin@brit-takehome-task.com")
    init()
    print("Superuser created")
