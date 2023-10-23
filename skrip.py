from playwright.sync_api import sync_playwright


def skrin_photo():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto('https://kun.uz/news/category/jahon', wait_until='load')
        elements = page.query_selector_all('img')
        image_url = elements[2].get_attribute('src')
        page.goto(image_url)
        page.screenshot(path='kun_uz_image.png')
        browser.close()