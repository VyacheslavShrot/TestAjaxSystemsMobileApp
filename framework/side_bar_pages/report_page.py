from appium.webdriver.common.appiumby import AppiumBy

from framework.page import Page


class ReportPage(Page):
    _report_title = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"]')

    @property
    def loaded(self) -> bool:
        return self.is_element_displayed(*self._report_title)

    def find_report_title(self) -> bool:
        report_title = self.is_element_displayed(*self._report_title)
        if not report_title:
            return False

        return True
