from appium.webdriver.common.appiumby import AppiumBy


class Buttons:

    def __init__(self, index: int):
        self.index = index

    def button(self) -> tuple:
        return (AppiumBy.XPATH,
                f'(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[{self.index}]/android.view'
                f'.View/android.view.View/android.widget.Button')

    def surveillance_button(self) -> tuple:
        return AppiumBy.XPATH, f'(//android.view.View[@resource-id="com.ajaxsystems:id/atomTitle"])[{self.index}]'

    def terms_button(self) -> tuple:
        return AppiumBy.XPATH, f'(//android.view.View[@resource-id="com.ajaxsystems:id/atomTitle"])[{self.index}]'
