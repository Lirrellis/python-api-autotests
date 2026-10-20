import pytest
import requests

@pytest.fixture(scope="function")
def api_base_url():
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

@pytest.mark.parametrize("number", [1, 2, 3])
def test_example(number):
    assert number > 0

@pytest.fixture(scope="function")
def shop_url():
    print("Подготовка")
    yield "https://www.saucedemo.com/"
    print("Очистка")