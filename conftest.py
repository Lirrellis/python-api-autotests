import pytest
import requests

@pytest.fixture(scope="function")
def base_url():
    print("Подготовка")
    yield "https://jsonplaceholder.typicode.com"
    print("Очистка")

@pytest.fixture
def api_session():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    print("Сессия создана")
    yield session
    session.close()
    print("Сессия закрыта")