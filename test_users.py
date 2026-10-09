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


def test_get_all_users():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 10
    for user in data:
        assert "id" in user
        assert isinstance(user["id"], int)
        assert "email" in user
        assert isinstance(user["email"], str)
        assert user["email"] != ""


def test_get_posts_by_user_2():
    params = {"userId": 2}
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params=params
    )

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    for post in data:
        assert "userId" in post
        assert post["userId"] == params["userId"]
        assert "title" in post
        assert isinstance(post["title"], str)
        assert post["title"] != ""


def test_get_comments_by_post():
    params = {"postId": 3}
    response = requests.get(
        "https://jsonplaceholder.typicode.com/comments",
        params=params
    )
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    for comment in data:
        assert "postId" in comment
        assert comment["postId"] == params["postId"]
        assert "id" in comment
        assert type(comment["id"]) is int
        assert comment["id"] > 0
        assert "email" in comment
        check_non_empty_string(comment["email"])
        assert "body" in comment
        check_non_empty_string(comment["body"])


def check_non_empty_string(value):
    assert isinstance(value, str)
    assert value.strip() != ""


def test_create_post_3():
    payload = {
        "title": "API automation practice",
        "body": "Testing POST requests with pytest",
        "userId": 3
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    data = response.json()
    assert response.status_code == 201

    assert "title" in data
    check_non_empty_string(data["title"])
    assert data["title"] == payload["title"]
    assert "body" in data
    check_non_empty_string(data["body"])
    assert data["body"] == payload["body"]
    assert "userId" in data
    assert type(data["userId"]) is int
    assert data["userId"] > 0
    assert data["userId"] == payload["userId"]
    assert "id" in data
    assert type(data["id"]) is int
    assert data["id"] > 0