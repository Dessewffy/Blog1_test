from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Blog:
    def __init__(self, browser: Chrome):
        self.browser = browser
        self.url = "http://ec2-3-120-40-183.eu-central-1.compute.amazonaws.com"
        # "http://localhost:4200/registration"

    def refresh(self):
        self.browser.refresh()

    def save_screen(self, path):
        self.browser.get_screenshot_as_file(path)
    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        self.browser.close()
# Regisztrációs elemek
    def registration_li(self):
        return self.browser.find_element(By.XPATH, '//li[@routerlink="registration"]')

    def firs_name_input(self):
        return self.browser.find_element(By.XPATH, '//input[@id="firstName"]')

    def last_name_input(self):
        return self.browser.find_element(By.XPATH, '//input[@id="lastName"]')

    def user_name_input(self):
        return self.browser.find_element(By.XPATH, '//input[@id="userName"]')

    def email_input(self):
        return self.browser.find_element(By.XPATH, '//input[@id="email"]')

    def password_input(self):
        return self.browser.find_element(By.XPATH, '//input[@id="password"]')

    def conf_password_input(self):
        return self.browser.find_element(By.XPATH, '//input[@id="confirmPassword"]')

    def submit_btn(self):
        return self.browser.find_element(By.XPATH, '//button[@id="submitButton"]')

    def expected_registration_text(self):
        return self.browser.find_element(By.XPATH, '//h3[@class="my-3"]')
 # Login elemek
    
    def log_in_link(self):
        return self.browser.find_element(By.XPATH, '//li[@routerlink="login"]')
    
    def log_in_text(self):
        assert_text = self.browser.find_element(By.XPATH,'//h3[@class="mb-4"]')
        return assert_text.text

    def log_in_us_name(self):
        return self.browser.find_element(By.ID, 'userName')
    
    def log_in_us_password(self):
        return self.browser.find_element(By.ID, 'password')
    
    def log_in_btn(self):
        return self.browser.find_element(By.ID, 'loginButton')