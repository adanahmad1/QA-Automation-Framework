from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with (sync_playwright() as p):
    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/login")

    print(page.title())

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.locator("#flash")).to_contain_text(["You logged into a secure area!\n"])

    page.screenshot(
        path="full1.png",
        full_page=True
    )
    page.close()
