import requests
from sklearn.utils._repr_html import params


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

def test_get_post(base_url, api_session):

        response = api_session.get(f"{base_url}/posts/5")

        data = response.json()

        assert response.status_code == 200
        assert "X-Test" not in api_session.headers
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

def test_get_user_2(base_url, api_session):

    response = api_session.get(f"{base_url}/users/2")
    api_session.headers["X-Test"] = "hello"
    data = response.json()

    assert response.status_code == 200

    assert data["id"] == 2
    assert isinstance(data["email"], str)
    assert data["email"] != ""
    assert api_session.headers["Accept"] == "application/json"
    assert response.request.headers["Accept"] == "application/json"

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


def test_update_post():
    payload = {
        "id": 5,
        "title": "Updated by autotest",
        "body": "Learning PUT requests",
        "userId": 1
    }
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/5",
        json=payload
    )

    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert data["id"] == payload["id"]
    assert "title" in data
    assert data["title"] == payload["title"]
    check_non_empty_string(data["title"])
    assert "body" in data
    assert data["body"] == payload["body"]
    check_non_empty_string(data["body"])
    assert "userId" in data
    assert data["userId"] == payload["userId"]


def test_patch_post():
    payload = {
        "title": "Changed with PATCH"
    }

    original_response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/5"
    )
    original_data = original_response.json()

    response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/5",
        json=payload
    )

    assert original_response.status_code == 200
    assert response.status_code == 200
    data = response.json()

    assert "id" in original_data
    assert original_data["id"] == 5
    assert "title" in original_data
    check_non_empty_string(original_data["title"])
    assert "body" in original_data
    assert "userId" in original_data

    assert "id" in data
    assert data["id"] == original_data["id"]
    assert "title" in data
    assert data["title"] == payload["title"]
    check_non_empty_string(data["title"])
    assert "body" in data
    assert data["body"] == original_data["body"]
    assert "userId" in data
    assert data["userId"] == original_data["userId"]

def test_delete_post():
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/5"
    )

    assert response.status_code == 200
    data = response.json()

    assert data == {}


def test_get_nonexistent_user(base_url, api_session):
    response = api_session.get(f"{base_url}/users/999999")
    data = response.json()

    assert response.status_code == 404
    assert data == {}

def test_get_nonexistent_post(base_url, api_session):
    response = api_session.get(f"{base_url}/posts/999999")
    data = response.json()

    assert response.status_code == 404
    assert data == {}
    assert response.elapsed.total_seconds() < 5

def test_posts_belong_to_user(base_url, api_session):
    response = api_session.get(f"{base_url}/posts?userId=3")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    for post in data:
        assert "userId" in post
        assert post["userId"] == 3
        check_non_empty_string(post["title"])
        check_non_empty_string(post["body"])

def test_comments_match_post(base_url, api_session):

    response_post = api_session.get(f"{base_url}/posts/5")
    data1 = response_post.json()
    response_comment = api_session.get(f"{base_url}/comments?postId={data1['id']}")
    data2 = response_comment.json()

    assert response_post.status_code == 200

    assert response_comment.status_code == 200

    assert isinstance(data2, list)
    assert len(data2) > 0
    for comment in data2:
        assert "postId" in comment
        assert comment["postId"] == data1["id"]

def test_create_post_response(base_url, api_session):
    payload = {
        "title": "API automation practice",
        "body": "Testing POST requests with pytest",
        "userId": 3
    }
    response = api_session.post(f"{base_url}/posts", json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data
    assert type(data["id"]) is int


def test_user_required_fields(base_url, api_session):
    response = api_session.get(f"{base_url}/users/1")
    data = response.json()
    required_fields = {
        "id", "name", "username", "email",
        "address", "phone", "website", "company"
    }

    assert response.status_code == 200
    assert required_fields.issubset(data.keys())