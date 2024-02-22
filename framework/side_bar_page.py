from appium.webdriver.common.appiumby import AppiumBy

from framework.page import Page


class SideBarPage(Page):
    _settings = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]')
    _help = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Help"]')
    _report = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"]')
    _surveillance = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Video Surveillance"]')

    _hub = (AppiumBy.XPATH, '//android.widget.Button')

    _terms = (AppiumBy.ID, 'com.ajaxsystems:id/documentation_text')

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._settings)

    def click_settings(self) -> None:
        self.click_element(self._settings)

    def click_help(self) -> None:
        self.click_element(self._help)

    def click_report(self) -> None:
        self.click_element(self._report)

    def click_surveillance(self) -> None:
        self.click_element(self._surveillance)

    def click_hub(self) -> None:
        self.click_element(self._hub)

    def click_terms(self) -> None:
        self.click_element(self._terms)
