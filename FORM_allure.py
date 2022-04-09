import AllureReports
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_positive_form_submission(self):
        driver = self.driver
        driver.get("https://form.123formbuilder.com/5012215")
        self.driver.maximize_window()
        print(driver.title)

        # fill the form
        # personal information
        driver.find_element(By.XPATH, "//h1[contains(text(),'Order Form')]")
        driver.find_element(By.XPATH, "//*[@placeholder='First']").send_keys("test")
        driver.find_element(By.XPATH, "//*[@placeholder='Last']").send_keys("fortest")
        driver.find_element(By.XPATH, "//*[@type='email']").send_keys("testfortest@gmail.com")
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'### ### #### ')]").send_keys("3434343434")

        # order information
        driver.find_element(By.XPATH, "//span[@data-role='option-text'][contains(.,'# Product 1')]").click()
        driver.find_element(By.XPATH, "//input[contains(@type,'number')]").send_keys("4")

        # ship date
        element = driver.find_element(By.ID, "date-00000012-month")
        action = ActionChains(driver)
        action.click(on_element=element)
        action.send_keys("03")
        action.perform()

        element = driver.find_element(By.ID, "date-00000012-day")
        action = ActionChains(driver)
        action.click(on_element=element)
        action.send_keys("22")
        action.perform()

        element = driver.find_element(By.ID, "date-00000012-year")
        action = ActionChains(driver)
        action.click(on_element=element)
        action.send_keys("2022")
        action.perform()

        # address
        driver.find_element(By.XPATH, "//*[@placeholder='Street Address']").send_keys("alt street")
        driver.find_element(By.XPATH, "//*[@placeholder='Street Address Line 2']").send_keys("apt 99")
        driver.find_element(By.XPATH, "//*[@placeholder='City']").send_keys("Los Angeles")
        driver.find_element(By.XPATH, "//*[@placeholder='Region']").send_keys("California")
        driver.find_element(By.XPATH, "//*[@placeholder='Postal / Zip Code']").send_keys("90031")
        driver.find_element(By.XPATH, "//*[@placeholder='Country']").send_keys("uni")
        driver.find_element(By.XPATH, "//div[@data-index='240'][contains(.,'United States')]").click()
        driver.find_element(By.XPATH, "//*[@data-type='dropdown']").click()
        driver.find_element(By.XPATH, "//*[@value='Choice2']").click()
        driver.find_element(By.XPATH, "(//label[@data-role='checkbox'])[2]").click()
        driver.find_element(By.XPATH, "(//label[@data-role='checkbox'])[3]").click()

        # captcha iframe
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        # clack checkbox
        driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()

        print("The form is filled")

        driver.quit()

if __name__ == "__main__":
    unittest.main(AllureReports)

