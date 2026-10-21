import playwright
import pytest
import requests
# import chromium
from playwright.sync_api import expect

def test_open_page(page):
    page.goto("https://example.com")

    assert page.title() == "Example Domain"
    print(page.locator("body > p:nth-child(3)").inner_text())
    print(page.evaluate("navigator.language"))

# def test_open_page(page):
#     print("1. Начинаю открывать сайт")
#     page.goto("https://example.com")
#
#     print("2. Сайт открылся")
#     assert page.title() == "Example Domain"
#
#     print("3. Проверяю h1")
#     assert page.locator("h1").inner_text() == "Example Domain"


def test_login(page, shop_url):
    page.goto(shop_url)
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    page.wait_for_url("**/inventory.html")
    expect(page.locator("[data-test=\"title\"]")).to_have_text("Products")


@pytest.mark.parametrize(
    "password, expected_error",
    [
        ("wrong_password", "Epic sadface: Username and password do not match any user in this service"),
        ("", "Epic sadface: Password is required"),
    ]
)
def test_login_negative(page, shop_url, password, expected_error):
    page.goto(shop_url)
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill(password)
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_have_text(expected_error)
    expect(page).to_have_url(shop_url)

def test_inventory_items(page, shop_url):
    page.goto(shop_url)
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    page.wait_for_url("**/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")
    # page.pause()
    expect(page.locator('[data-test="inventory-item"]')).to_have_count(6)
    expect(page.locator('[data-test="inventory-item-name"]').first).to_have_text("Sauce Labs Backpack")
    for item in page.locator('[data-test="inventory-item-name"]').all():
        name = item.inner_text()
        assert len(name.strip()) > 0
        print(name)