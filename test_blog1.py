import configuration as config
from POM import Blog


class TestBlog():
    def setup_method(self):
        self.page = Blog(config.get_preconfigured_chrome_driver())
        self.page.open()
        assert self.page.browser.title == "Blog1Project"


    def teardown_method(self):
         self.page.close()

    # Regisztrációnak a tesztjei
    def test_registration_valid(self):
        self.page.registration_li().click()

        assert self.page.expected_registration_text().text == "Registration"

        self.page.firs_name_input().send_keys("Aurel")

        self.page.last_name_input().send_keys("Dessewffy")

        self.page.user_name_input().send_keys("Valdis")

        self.page.email_input().send_keys("yokatov131@oprevolt.com")

        # 8 karakter kis és nagybetű meg számok + 1 speciális karakter
        self.page.password_input().send_keys("Dessewffy1842@")

        # CI/CD-nél nem fog működni
        img_path = 'C:/Users/benja/Downloads/800px-Barabás_dessewffy_emil.jpg'
       # self.page.reg_file_upload().send_keys(img_path)

        self.page.conf_password_input().send_keys("Dessewffy1842@")

        self.page.save_screen("C:/Users/benja/Project/blog-I-project/Tests/Benjamin/screens")

        s_btn = self.page.submit_btn()
        assert s_btn.is_displayed()

        s_btn.click()
    # regisztráció invalid adatokkal
    def test_registration_invalid(self):
        self.page.registration_li().click()

        assert self.page.expected_registration_text().text == "Registration"

        self.page.firs_name_input().send_keys("a")

        self.page.last_name_input().send_keys("b")

        self.page.user_name_input().send_keys("c")

        self.page.email_input().send_keys("lecey60242@alibrscom")

        # 8 karakter kis és nagybetű meg számok + 1 speciális karakter
        self.page.password_input().send_keys("Dessewffy1842@")

        self.page.conf_password_input().send_keys("Dessewffy1842@")

        self.page.save_screen("screens/invalid_registration.png")

        s_btn = self.page.submit_btn()
        assert s_btn != s_btn.is_displayed()



    def test_log_in_valid(self):
        self.page.log_in_link().click()

        #Sikeres navigáció ellenőrzése
        login_assert = self.page.log_in_text()

        assert login_assert == "Log In"

        self.page.log_in_us_name().send_keys("Alysha.Hahn98")

        self.page.log_in_us_password().send_keys("Potter3@$!%*?&(){}_")

        self.page.log_in_btn().click()
