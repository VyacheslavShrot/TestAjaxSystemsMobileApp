from framework.page import Page
from utils.buttons import Buttons


class SurveillancePage(Page):
    _hikvision_button = Buttons(1).surveillance_button()
    _uniview_button = Buttons(2).surveillance_button()

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._hikvision_button)

    def find_hikvision_button(self) -> bool:
        hikvision_button = self.is_element_displayed(*self._hikvision_button)
        if not hikvision_button:
            return False

        return True

    def click_hikvision_button(self) -> None:
        self.click_element(self._hikvision_button)

    def click_uniview_button(self) -> None:
        self.click_element(self._uniview_button)
