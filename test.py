from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set headless=True to run in background
        page = browser.new_page()

        # Step 1: Go to saucedemo
        page.goto("https://www.saucedemo.com")

        # Step 2: Log in
        page.fill('input[data-test="username"]', 'standard_user')
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')

        # Step 3: Add two items to the cart
        page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
        page.click('button[data-test="add-to-cart-sauce-labs-bike-light"]')

        # Step 4: Go to the cart
        page.click('.shopping_cart_link')

        # Step 5: Take a screenshot of the cart
        page.screenshot(path="cart.png")

        # Optional: Pause to observe (if not headless)
        page.wait_for_timeout(3000)

        browser.close()

if __name__ == "__main__":
    run()
