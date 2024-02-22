from framework.page import Page
from utils.buttons import Buttons


class TermsPage(Page):
    _user_agreement_button = Buttons(1).terms_button()
    _privacy_policy_button = Buttons(2).terms_button()
    _privacy_notice_button = Buttons(3).terms_button()

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._user_agreement_button)

    def find_user_agreement_button(self) -> bool:
        user_agreement_button = self.is_element_displayed(*self._user_agreement_button)
        if not user_agreement_button:
            return False

        return True

    def click_user_agreement_button(self) -> None:
        self.click_element(self._user_agreement_button)

    def click_privacy_policy_button(self) -> None:
        self.click_element(self._privacy_policy_button)

    def click_privacy_notice_button(self) -> None:
        self.click_element(self._privacy_notice_button)
