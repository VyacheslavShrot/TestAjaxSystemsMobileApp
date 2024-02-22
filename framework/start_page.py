from framework.page import Page
from utils.buttons import Buttons


class StartPage(Page):
    _login_button = Buttons(1).button()
    _register_button = Buttons(2).button()

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._login_button)

    def click_login_button(self) -> None:
        self.click_element(self._login_button)

    def click_register_button(self) -> None:
        self.click_element(self._register_button)
