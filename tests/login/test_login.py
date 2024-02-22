import logging

import pytest
from appium.webdriver.webdriver import WebDriver

from framework import StartPage
from framework.login_page import LoginPage, LoginErrorPage
from framework.main_page import MainPage


class TestLogin:

    @pytest.mark.parametrize(
        "email, password, expected_success", [
            ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),  # Successful login
            ("qa.ajax.app.automation@gmail.com", "incorrect_password", False),  # Incorrect password
            ("incorrect_email@gmail.com", "qa_automation_password", False),  # Incorrect email
            ("incorrect_email@gmail.com", "incorrect_password", False),  # Incorrect password and email
        ]
    )
    def test_login(self, start_fixture: StartPage, driver: WebDriver, email: str, password: str, expected_success: bool):
        try:
            start_page = start_fixture
            login_page = LoginPage(driver)
            login_error_page = LoginErrorPage(driver)
            main_page = MainPage(driver)

            logging.info(f"Test case for login with email '{email}' and password '{password}' started")

            """
                        Action on the Start Page
            """
            logging.info(f"Click on the button and go to the Login page")
            start_page.wait_for_page_to_load().click_login_button()

            """
                        Action on the Login Page
            """
            logging.info(f"Enter user data and try to perform authorization")
            login_page.wait_for_page_to_load().login(email=email, password=password).click_show_password().click_login_button()

            """
                        Login Status Check
            """
            if expected_success:
                logging.info(f"Check if the login is SUCCESSFUL")
                assert main_page.wait_for_page_to_load().find_side_bar(), "Expected SUCCESSFUL Login"
            else:
                logging.info(f"Check if the login is FAIL")
                assert login_error_page.wait_for_page_to_load().find_login_error(), "Expected Login to FAIL"
        except Exception as e:
            logging.error(f"An unexpected error occurred during a test with an email '{email}' and password '{password}' | {e}")
