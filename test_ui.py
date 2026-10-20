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


    # <input class="input_error form_input" placeholder="Username" aria-label="Username" data-test="username" id="user-name" autocorrect="off" autocapitalize="none" type="text" value="" name="user-name">