from playwright.sync_api import sync_playwright


def get_information():
    url = 'https://kun.uz/news/category/jahon'
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url, wait_until="load")
        repo = page.query_selector_all('.top-news__big')
        for i in repo:
            information1 = i.text_content().split()[2][10:]
            information2 = i.text_content().split()[3:]
            year = i.text_content().split()[2][0:10]
            date = i.text_content().split()[0]
        datas = {
            "date": date,
            "year": year,
            "info1": information1,
            "info2": information2
        }
        return datas

