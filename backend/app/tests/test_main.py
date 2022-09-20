from app.data import models
from app.data.repositories.item_repository import get_items


def test_read_main(client):
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_load_items(test_db, test_items):
    items = get_items(test_db)
    assert items
