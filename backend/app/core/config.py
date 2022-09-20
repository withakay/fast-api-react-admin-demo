import os

# TODO: Use pydantic for settings

PROJECT_NAME = "brit-takehome-task"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

API_V1_STR = "/api/v1"
