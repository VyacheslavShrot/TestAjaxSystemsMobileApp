from appium.webdriver.webdriver import WebDriver

from framework import StartPage
from framework.login_page import LoginPage
from framework.main_page import MainPage
from framework.side_bar_page import SideBarPage
from framework.side_bar_pages.help_page import HelpPage
from framework.side_bar_pages.hub_page import HubPage
from framework.side_bar_pages.report_page import ReportPage
from framework.side_bar_pages.settings_page import SettingsPage
from framework.side_bar_pages.surveillance_page import SurveillancePage
from framework.side_bar_pages.terms_page import TermsPage


class SideBar:

    def __init__(self, start_fixture: StartPage, driver: WebDriver):
        self.start_fixture = start_fixture
        self.driver = driver

    def get_data(self) -> tuple:
        return (
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            SideBarPage(self.driver),
            self.start_fixture,
            LoginPage(self.driver),
            MainPage(self.driver),
            SettingsPage(self.driver),
            HelpPage(self.driver),
            ReportPage(self.driver),
            SurveillancePage(self.driver),
            HubPage(self.driver),
            TermsPage(self.driver)
        )

    @classmethod
    def jump_to_sidebar(cls, start_page: StartPage, login_page: LoginPage, main_page: MainPage, email: str, password: str) -> None:
        start_page.wait_for_page_to_load().click_login_button()  # Login step 1
        login_page.wait_for_page_to_load().login(email=email, password=password).click_show_password().click_login_button()  # Login step 2

        main_page.wait_for_page_to_load().click_side_bar()

    @classmethod
    def check_settings_page(cls, side_bar_page: SideBarPage, settings_page: SettingsPage) -> bool:
        side_bar_page.wait_for_page_to_load().click_settings()
        return settings_page.wait_for_page_to_load().find_user_icon()

    @classmethod
    def check_help_page(cls, side_bar_page: SideBarPage, help_page: HelpPage) -> bool:
        side_bar_page.wait_for_page_to_load().click_help()
        return help_page.wait_for_page_to_load().find_toolbar_title()

    @classmethod
    def check_report_page(cls, side_bar_page: SideBarPage, report_page: ReportPage) -> bool:
        side_bar_page.wait_for_page_to_load().click_report()
        return report_page.wait_for_page_to_load().find_report_title()

    @classmethod
    def check_surveillance_page(cls, side_bar_page: SideBarPage, surveillance_page: SurveillancePage) -> bool:
        side_bar_page.wait_for_page_to_load().click_surveillance()
        return surveillance_page.wait_for_page_to_load().find_hikvision_button()

    @classmethod
    def check_hub_page(cls, side_bar_page: SideBarPage, hub_page: HubPage) -> bool:
        side_bar_page.wait_for_page_to_load().click_hub()
        return hub_page.wait_for_page_to_load().find_hub_title()

    @classmethod
    def check_terms_page(cls, side_bar_page: SideBarPage, terms_page: TermsPage) -> bool:
        side_bar_page.wait_for_page_to_load().click_terms()
        return terms_page.wait_for_page_to_load().find_user_agreement_button()
