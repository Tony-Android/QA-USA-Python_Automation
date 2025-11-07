from data import URBAN_ROUTES_URL
from helpers import is_url_reachable
from selenium import webdriver
webdriver.Chrome()


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to Urban Route Server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    def test_set_route(self):

        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self):

        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):

        # Add in S8
        print("function created for fill phone number")
        pass

    def test__fill_card(self):

        # Add in S8
        print("function created for set route")
        pass

    def test_comment_for_driver(self):

        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):

        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            # Add in S8
            print("function created for order 2 ice creams")
            pass

    def test_car_search_model_appears(self):

        # Add in S8
        print("function created for car search model appears")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()