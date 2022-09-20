from decimal import Decimal

from app.data import models


def test_get_items(client, test_items, superuser_token_headers):
    response = client.get("/api/v1/items", headers=superuser_token_headers)
    assert response.status_code == 200
    response = response.json()[0]
    expected_response = {
        "id": 1,
        "name": "foo",
        "price": 1.50,
    }

    assert sorted(response.keys()) == sorted(expected_response.keys())
    for k in response.keys():
        assert expected_response[k] == response[k]


def test_get_item(client, test_items, superuser_token_headers):
    response = client.get(
        f"/api/v1/items/{test_items[0].id}", headers=superuser_token_headers
    )
    assert response.status_code == 200
    response = response.json()
    expected_response = {
        "id": 1,
        "name": "foo",
        "price": 1.50,
    }


def test_delete_item(client, test_items, test_db, superuser_token_headers):
    item_to_delete = test_items[0]
    response = client.delete(
        f"/api/v1/items/{item_to_delete.id}", headers=superuser_token_headers
    )
    assert response.status_code == 200
    assert (
        test_db.query(models.Item).filter_by(id=item_to_delete.id).all() == []
    )


def test_edit_item(client, test_items, superuser_token_headers):
    test_item = test_items[0]
    new_item_values = {
        "name": "test_item",
        "price": 0,
    }

    response = client.put(
        f"/api/v1/items/{test_item.id}",
        json=new_item_values,
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    new_item_values["id"] = test_item.id
    assert response.json() == new_item_values


def test_item_summary(client, test_items, superuser_token_headers):
    response = client.get(
        "/api/v1/items/summary", headers=superuser_token_headers
    )
    assert response.status_code == 200
    print(response.json())
    assert response.json()["total"] == 1000349.44



