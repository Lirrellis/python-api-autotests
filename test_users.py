import requests


def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"

def test_create_post():
        payload = {
            "title": "Hello",
            "body": "My first autotest",
            "userId": 1,
        }

        response = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            json=payload
        )

        assert response.status_code == 201

        data = response.json()

        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]
        assert data["id"] == 101

def test_get_post():

        response = requests.get("https://jsonplaceholder.typicode.com/posts/5")

        data = response.json()

        assert response.status_code == 200
        assert data["id"] == 5
        assert data["userId"] == 1
        assert isinstance(data["title"], str)
        assert isinstance(data["body"], str)

def test_get_posts_by_user():
        params = {
            "userId": 1
        }

        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            params=params
        )

        data = response.json()

        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) > 0
        for post in data:
            assert post["userId"] == params["userId"]

def test_get_user_2():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/2"
    )
    data = response.json()

    assert response.status_code == 200

    assert data["id"] == 2
    assert isinstance(data["email"], str)
    assert data["email"] != ""

def test_create_post_2():
    payload = {
        "title": "Learning Python",
        "body": "My first API autotests",
        "userId": 2
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data
    assert isinstance(data["id"], int)
