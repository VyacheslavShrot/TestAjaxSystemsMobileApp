from appium.webdriver.common.appiumby import AppiumBy

from framework.page import Page


class HelpPage(Page):
    _toolbar_title = (AppiumBy.ID, 'com.ajaxsystems:id/toolbarTitle')

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._toolbar_title)

    def find_toolbar_title(self) -> bool:
        toolbar_title = self.is_element_displayed(*self._toolbar_title)
        if not toolbar_title:
            return False

        return True
