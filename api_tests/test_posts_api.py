import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
POST_ID = 1

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/{POST_ID}")
    assert response.status_code == 200
    assert response.json()["id"] == POST_ID

def test_create_post():
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"

def test_update_post():
    data = {"title": "updated"}
    response = requests.patch(f"{BASE_URL}/posts/{POST_ID}", json=data)
    assert response.status_code == 200
    assert response.json()["title"] == "updated"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/{POST_ID}")
    assert response.status_code == 200
