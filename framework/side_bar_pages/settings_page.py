from appium.webdriver.common.appiumby import AppiumBy

from framework.page import Page


class SettingsPage(Page):
    _user_icon = (AppiumBy.XPATH, '//android.view.View[@resource-id="com.ajaxsystems:id/icon"]')

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._user_icon)

    def find_user_icon(self) -> bool:
        user_icon = self.is_element_displayed(*self._user_icon)
        if not user_icon:
            return False

        return True
