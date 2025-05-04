import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os

from config import settings
from selene_in_action import utils

from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # 'platformName': 'android',
        'platformVersion': settings.android_platform_version,
        'deviceName': settings.android_device_name,

        # Set URL of the application under test
        'app':  settings.app, # 'bs://sample.app',

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Set your access credentials
            'userName': settings.bstack_username,
            'accessKey': settings.bstack_access_key,
        }
    })

    # browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    # browser.config.driver_options = options

    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            settings.browserstack_url,
            options=options
        )

    browser.config.timeout = settings.timeout

    # Декоратор для логгирования каждого шага в allure
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    with allure.step('Take screenshot'):
        utils.allure.attach_screenshot(browser)

    with allure.step('Save xml report'):
        utils.allure.attach_xml(browser)


    session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

    utils.allure.attach_bstack_video(session_id)


