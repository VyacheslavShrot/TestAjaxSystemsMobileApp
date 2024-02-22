import subprocess
import time

import pytest
from appium import webdriver
from appium.options.common import AppiumOptions

from framework import StartPage
from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='function')
def driver(run_appium_server):
    option = AppiumOptions().load_capabilities(android_get_desired_capabilities())
    driver = webdriver.Remote('http://localhost:4723', options=option)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def start_fixture(driver):
    yield StartPage(driver)
