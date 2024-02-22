from typing import Union

from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    _back = (AppiumBy.XPATH, '//android.widget.ImageButton[@resource-id="com.ajaxsystems:id/back"]')

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def wait_for_page_to_load(self) -> 'Page':
        self.wait.until(lambda _: self.loaded)
        return self

    @property
    def loaded(self) -> bool:
        raise NotImplementedError('Each Page should implement its own loaded() method')

    def is_element_displayed(self, strategy: Union[AppiumBy, str], locator: str) -> bool:
        try:
            return self.driver.find_element(strategy, locator).is_displayed()
        except NoSuchElementException:
            return False

    def find_element(self, locator: tuple) -> WebElement | bool:
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return False

    def click_element(self, locator: tuple) -> None:
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator: tuple, text: str) -> None:
        element = self.find_element(locator)
        element.send_keys(text)

    def click_back(self) -> None:
        self.click_element(self._back)
