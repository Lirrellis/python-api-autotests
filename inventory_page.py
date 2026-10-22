
class InventoryPage:
    def __init__(self, page):
        self.page = page

    def get_items(self):
        return  self.page.locator('[data-test="inventory-item"]')

    def get_item_names(self):
        return self.page.locator('[data-test="inventory-item-name"]')

    def get_title(self):
        return self.page.locator('[data-test="title"]')

    def get_prices(self):
        return self.page.locator('[data-test="inventory-item-price"]')