# saucedemo_automation.py
import json
import logging
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# Config loading
def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Page Object Models
class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill('input[data-test="username"]', username)
        self.page.fill('input[data-test="password"]', password)
        self.page.click('input[data-test="login-button"]')
        logging.info("Logged in as %s", username)


class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_items_to_cart(self):
        self.page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
        self.page.click('button[data-test="add-to-cart-sauce-labs-bike-light"]')
        logging.info("Items added to cart")

    def go_to_cart(self):
        self.page.click('.shopping_cart_link')
        logging.info("Navigated to cart")


class CartPage:
    def __init__(self, page):
        self.page = page

    def proceed_to_checkout(self):
        self.page.click('button[data-test="checkout"]')
        logging.info("Clicked checkout")


class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.fill('input[data-test="firstName"]', first_name)
        self.page.fill('input[data-test="lastName"]', last_name)
        self.page.fill('input[data-test="postalCode"]', postal_code)
        self.page.click('input[data-test="continue"]')
        logging.info("Filled in checkout info")

    def get_total_price(self):
        return self.page.locator('.summary_total_label').inner_text()

    def finish_order(self):
        self.page.click('button[data-test="finish"]')
        logging.info("Order finished")

    def get_confirmation(self):
        return self.page.locator('.complete-header').inner_text()


# Main automation flow
def run():
    config = load_config()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto(config["base_url"])
            page.screenshot(path="0_home.png")

            login = LoginPage(page)
            login.login(config["username"], config["password"])
            page.screenshot(path="1_logged_in.png")

            inventory = InventoryPage(page)
            inventory.add_items_to_cart()
            page.screenshot(path="2_items_added.png")
            inventory.go_to_cart()

            cart = CartPage(page)
            page.screenshot(path="3_cart_view.png")
            cart.proceed_to_checkout()

            checkout = CheckoutPage(page)
            checkout.fill_checkout_info("Dhieu", "David", "00255")
            page.screenshot(path="4_checkout_info.png")

            total = checkout.get_total_price()
            logging.info("Total price extracted: %s", total)
            page.screenshot(path="5_checkout_summary.png")

            checkout.finish_order()
            confirmation = checkout.get_confirmation()
            logging.info("Order confirmation: %s", confirmation)
            page.screenshot(path="6_order_complete.png")

            # Save result
            with open("order_summary.json", "w") as f:
                json.dump({"total": total, "status": confirmation}, f, indent=2)

        except PlaywrightTimeoutError as e:
            logging.error("Timeout occurred: %s", e)
            page.screenshot(path="error_timeout.png")
        except Exception as e:
            logging.error("Unexpected error: %s", e)
            page.screenshot(path="error_unexpected.png")
        finally:
            browser.close()


if __name__ == "__main__":
    run()
