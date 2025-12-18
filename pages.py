import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

class UrbanRoutesPage:

    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    CALL_A_TAXI_BUTTON = (By.XPATH, "//button[text()='Call a taxi']")

    def __init__(self, driver):
        self.driver = driver

    def input_from_address(self, from_address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_address)
    def input_to_address(self, to_address):
        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def get_from_address(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")
    def get_to_address(self):
        return self.driver.find_element(*self.TO_FIELD).get_attribute("value")
    def click_call_a_taxi_button(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON).click()
