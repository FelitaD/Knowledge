from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(devtools=True)  # headless=True by default
    page = browser.new_page()
    page.goto('https://app2.bankin.com/signin')
    page.fill('#signin_email', <EMAIL>)
    page.fill('#signin_password', <PWD>)
    page.click('.btn fs1 fw6 mt3')
    page.screenshot(path='bankin_login.png')
    browser.close()