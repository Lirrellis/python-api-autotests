class LoginPage:
    def __init__(self, page):
        self.page = page


    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()