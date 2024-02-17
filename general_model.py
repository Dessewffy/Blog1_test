from datetime import datetime
from selenium import webdriver


class GeneralPage:

    def __init__(self, browser: webdriver.Chrome, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        self.browser.close()

    def refresh(self):
        self.browser.refresh()

    def save_screen(self, path):
        filename = f"{self.browser.title} - {datetime.now()}.png"
        print(f"Screenshot attempt: {path}\\{filename}")
        if not self.browser.save_screenshot(f"{path}\\{filename}"):
            print("Screenshot failed.")
        else:
            print("Screenshot saved successfully.")