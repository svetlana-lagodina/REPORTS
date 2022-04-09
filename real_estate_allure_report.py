import AllureReports
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_positive_form_submission(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        self.driver.maximize_window()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # find submit button
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

        # assert title
        assert 'California Real Estate' in driver.title
        print("The title of the page is:", driver.title)

        # fill up the form
        fields = driver.find_element(By.XPATH, "//input[@type='text']")
        fields.clear()
        driver.find_element(By.XPATH, "//*[@id='g2-name']").send_keys('test')
        driver.find_element(By.NAME, "g2-email").send_keys('test.fortest@gmail.com')
        driver.find_element(By.NAME, "g2-message").send_keys('please,text me')

        # click on the submit button
        driver.find_element(By.XPATH, "//button[@type='submit']").send_keys('\n')

        # find 'go back' button and click
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "go back"))).send_keys('\n')
            print("Go back link is on the page")
        except TimeoutException:
            print("Loading took too much time!")

        # find all images on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55 size-full']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34 size-full']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56 size-full']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30 size-full']")))
            print("All images are on the page")
        except TimeoutException:
            print("Check up images")

        # assert title
        assert 'California Real Estate' in driver.title
        print("The title of the page is:", driver.title)

    def test_negative_empty_fields(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        self.driver.maximize_window()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # find submit button
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

        # assert title
        assert 'California Real Estate' in driver.title
        print("The title of the page is:", driver.title)

        # clear form
        fields = driver.find_element(By.XPATH, "//input[@type='text']")
        fields.clear()

        # click on the submit button
        driver.find_element(By.XPATH, "//button[@type='submit']").send_keys('\n')

        # assert the form was not submitted
        try:
            driver.find_element(By.LINK_TEXT, 'go back')
            raise ValueError("Test failed")
        except NoSuchElementException:
            print("Test passed")

    def test_negative_invalid_email(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        self.driver.maximize_window()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # find submit button
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

        # assert title
        assert 'California Real Estate' in driver.title
        print("The title of the page is:", driver.title)

        # clear form and put invalid email
        fields = driver.find_element(By.XPATH, "//input[@type='text']")
        fields.clear()
        driver.find_element(By.XPATH, "//*[@id='g2-name']").send_keys('test')
        driver.find_element(By.NAME, "g2-email").send_keys('/@gmail.co')
        driver.find_element(By.NAME, "g2-message").send_keys('please,text me')

        # click on the submit button
        driver.find_element(By.XPATH, "//button[@type='submit']").send_keys('\n')

        # assert the form was not submitted
        try:
            driver.find_element(By.LINK_TEXT, 'go back')
            raise ValueError("Test failed")
        except NoSuchElementException:
            print("Test passed")

    def test_header_links(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        self.driver.maximize_window()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # find submit button
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

        # assert title
        assert 'California Real Estate' in driver.title
        print("The title of the page is:", driver.title)

        # find header elements and get link values
        first_link = driver.find_element(By.XPATH, "//*[@aria-current='page']").get_attribute("href")
        second_link = driver.find_element(By.XPATH, "(//a[contains(.,'California Real Estate')])[1]").get_attribute("href")
        third_link = driver.find_element(By.CLASS_NAME, "custom-logo-link").get_attribute("href")
        example = "https://qasvus.wordpress.com/"

        # assert all links lead to the home page
        assert first_link==second_link==third_link==example
        print("Test passed")


class EdgeSearch(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Edge()

        def test_positive_form_submission(self):
            driver = self.driver
            driver.get('https://qasvus.wordpress.com/')
            self.driver.maximize_window()

            # set up wait time
            wait = WebDriverWait(driver, 3)

            # find submit button
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

            # assert title
            assert 'California Real Estate' in driver.title
            print("The title of the page is:", driver.title)

            # fill up the form
            fields = driver.find_element(By.XPATH, "//input[@type='text']")
            fields.clear()
            driver.find_element(By.XPATH, "//*[@id='g2-name']").send_keys('test')
            driver.find_element(By.NAME, "g2-email").send_keys('test.fortest@gmail.com')
            driver.find_element(By.NAME, "g2-message").send_keys('please,text me')

            # click on the submit button
            driver.find_element(By.XPATH, "//button[@type='submit']").send_keys('\n')

            # find 'go back' button and click
            try:
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "go back"))).send_keys('\n')
                print("Go back link is on the page")
            except TimeoutException:
                print("Loading took too much time!")

            # find all images on the page
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55 size-full']")))
                wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34 size-full']")))
                wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56 size-full']")))
                wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30 size-full']")))
                print("All images are on the page")
            except TimeoutException:
                print("Check up images")

            # assert title
            assert 'California Real Estate' in driver.title
            print("The title of the page is:", driver.title)

        def test_negative_empty_fields(self):
            driver = self.driver
            driver.get('https://qasvus.wordpress.com/')
            self.driver.maximize_window()

            # set up wait time
            wait = WebDriverWait(driver, 3)

            # find submit button
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

            # assert title
            assert 'California Real Estate' in driver.title
            print("The title of the page is:", driver.title)

            # clear form
            fields = driver.find_element(By.XPATH, "//input[@type='text']")
            fields.clear()

            # click on the submit button
            driver.find_element(By.XPATH, "//button[@type='submit']").send_keys('\n')

            # assert the form was not submitted
            try:
                driver.find_element(By.LINK_TEXT, 'go back')
                raise ValueError("The form was submitted. Test failed")
            except NoSuchElementException:
                print("Test passed")

        def test_negative_invalid_email(self):
            driver = self.driver
            driver.get('https://qasvus.wordpress.com/')
            self.driver.maximize_window()

            # set up wait time
            wait = WebDriverWait(driver, 3)

            # find submit button
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

            # assert title
            assert 'California Real Estate' in driver.title
            print("The title of the page is:", driver.title)

            # clear form and put invalid email
            fields = driver.find_element(By.XPATH, "//input[@type='text']")
            fields.clear()
            driver.find_element(By.XPATH, "//*[@id='g2-name']").send_keys('test')
            driver.find_element(By.NAME, "g2-email").send_keys('/@gmail.co')
            driver.find_element(By.NAME, "g2-message").send_keys('please,text me')

            # click on the submit button
            driver.find_element(By.XPATH, "//button[@type='submit']").click()

            # assert the form was not submitted
            try:
                driver.find_element(By.LINK_TEXT, 'go back')
                raise ValueError("The form was submitted. Test failed")
            except NoSuchElementException:
                print("Test passed")

        def test_header_links(self):
            driver = self.driver
            driver.get('https://qasvus.wordpress.com/')
            self.driver.maximize_window()

            # set up wait time
            wait = WebDriverWait(driver, 3)

            # find submit button
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

            # assert title
            assert 'California Real Estate' in driver.title
            print("The title of the page is:", driver.title)

            # find header elements and get link values
            first_link = driver.find_element(By.XPATH, "//*[@aria-current='page']").get_attribute("href")
            second_link = driver.find_element(By.XPATH, "(//a[contains(.,'California Real Estate')])[1]").get_attribute(
                "href")
            third_link = driver.find_element(By.CLASS_NAME, "custom-logo-link").get_attribute("href")
            example = "https://qasvus.wordpress.com/"

            # assert all links lead to the home page
            assert first_link == second_link == third_link == example
            print("Test passed")


        def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main(AllureReports)
