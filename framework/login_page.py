from appium.webdriver.common.appiumby import AppiumBy

from utils.buttons import Buttons
from .page import Page


class LoginPage(Page):
    _email_field = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]')
    _password_field = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]')

    _login_button = Buttons(4).button()

    _icon_password = (AppiumBy.XPATH, '//android.view.View[@resource-id="iconPassword"]')

    _forgot_password = Buttons(3).button()

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._email_field)

    def login(self, email: str, password: str) -> 'LoginPage':
        self.input_text(self._email_field, email)
        self.input_text(self._password_field, password)
        return self

    def click_login_button(self) -> None:
        self.click_element(self._login_button)

    def click_show_password(self) -> 'LoginPage':
        self.click_element(self._icon_password)
        return self

    def click_forgot_password(self) -> None:
        self.click_element(self._forgot_password)


class LoginErrorPage(LoginPage):
    _login_error = (AppiumBy.ID, 'com.ajaxsystems:id/snackbar_text')

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._login_error)

    def find_login_error(self) -> bool:
        login_error = self.is_element_displayed(*self._login_error)
        if not login_error:
            return False

        return True
