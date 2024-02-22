from appium.webdriver.common.appiumby import AppiumBy

from framework.page import Page


class HubPage(Page):
    _hub_title = (AppiumBy.ID, 'com.ajaxsystems:id/toolbarTitle')

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._hub_title)

    def find_hub_title(self) -> bool:
        hub_title = self.is_element_displayed(*self._hub_title)
        if not hub_title:
            return False

        return True
