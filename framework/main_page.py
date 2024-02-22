from appium.webdriver.common.appiumby import AppiumBy

from framework.page import Page


class MainPage(Page):
    _side_bar = (AppiumBy.ID, 'com.ajaxsystems:id/menuDrawer')

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._side_bar)

    def find_side_bar(self) -> bool:
        side_bar = self.is_element_displayed(*self._side_bar)
        if not side_bar:
            return False

        return True

    def click_side_bar(self) -> None:
        self.click_element(self._side_bar)
