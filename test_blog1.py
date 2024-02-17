import configuration as config
from POM import Blog


class TestBlog():
    def setup_method(self):
        self.page = Blog(config.get_preconfigured_chrome_driver())
        self.page.open()
        assert self.page.browser.title == "Blog1Project"


    def teardown_method(self):
         self.page.close()


    def test_log_in_valid(self):
        self.page.log_in_link().click()

        #Sikeres navigáció ellenőrzése
        login_assert = self.page.log_in_text()

        assert login_assert == "Log In"

        self.page.log_in_us_name().send_keys("Alysha.Hahn98")

        self.page.log_in_us_password().send_keys("Potter3@$!%*?&(){}_")

        self.page.log_in_btn().click()
