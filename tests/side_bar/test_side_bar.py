import logging

import pytest
from appium.webdriver.webdriver import WebDriver

from framework import StartPage
from utils.side_bar import SideBar


class TestSideBar:

    @pytest.mark.parametrize(
        "element", [
            "settings",
            "help",
            "report",
            "surveillance",
            "hub",
            "terms",
        ]
    )
    def test_elements_on_side_bar(self, start_fixture: StartPage, driver: WebDriver, element: str):
        try:
            side_bar = SideBar(start_fixture, driver)
            (
                email,
                password,
                side_bar_page,
                start_page,
                login_page,
                main_page,
                settings_page,
                help_page,
                report_page,
                surveillance_page,
                hub_page,
                terms_page
            ) = side_bar.get_data()

            logging.info(f"Test case for check element '{element}' in the sidebar started")

            """
                        Go to the SideBar Page
            """
            logging.info(f"Starting with a standard login")
            side_bar.jump_to_sidebar(start_page, login_page, main_page, email, password)

            """
                        Action on Elements from SideBar Page
            """
            logging.info(f"Check if the element '{element}' was successfully opened ")

            if element == "settings":  # Check Settings Page
                checked: bool = side_bar.check_settings_page(side_bar_page, settings_page)
                assert checked, "Expected SUCCESSFUL switch to Settings"

            if element == "help":  # Check Help Page
                checked: bool = side_bar.check_help_page(side_bar_page, help_page)
                assert checked, "Expected SUCCESSFUL switch to Help"

            if element == "report":  # Check Report Page
                checked: bool = side_bar.check_report_page(side_bar_page, report_page)
                assert checked, "Expected SUCCESSFUL switch to Report"

            if element == "surveillance":  # Check Video Surveillance Page
                checked: bool = side_bar.check_surveillance_page(side_bar_page, surveillance_page)
                assert checked, "Expected SUCCESSFUL switch to Video Surveillance"

            if element == "hub":  # Check Hub Page
                checked: bool = side_bar.check_hub_page(side_bar_page, hub_page)
                assert checked, "Expected SUCCESSFUL switch to Hub"

            if element == "terms":  # Check Terms Page
                checked: bool = side_bar.check_terms_page(side_bar_page, terms_page)
                assert checked, "Expected SUCCESSFUL switch to Terms"
        except Exception as e:
            logging.error(f"An unexpected error occurred during a test with an element '{element}' | {e}")
