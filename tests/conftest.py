import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support

import os
import sys

# Добавляем корневую директорию в sys.path для доступа к config.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings
from selene_in_action import utils

from appium import webdriver


def pytest_addoption(parser):
    parser.addoption('--platform', default='android', help='Specify platform: android, ios, or local/web')


@pytest.fixture(scope='session')
def platform(request):
    return request.config.getoption('--platform')


@pytest.fixture(scope='function', autouse=True)
def mobile_management(platform):
    """
    Общая фикстура для управления мобильными сессиями, которая поддерживает обе платформы
    """
    if platform.lower() == 'android':
        options = UiAutomator2Options().load_capabilities({
            'platformVersion': settings.android_platform_version,
            'deviceName': settings.android_device_name,

            'app': settings.app,# 'bs://sample.app',

            'bstack:options': {
                'projectName': 'Python Mobile Project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'Android Test Session',
                'userName': settings.bstack_username,
                'accessKey': settings.bstack_access_key,
            }
        })
    elif platform.lower() == 'ios':
        options = XCUITestOptions().load_capabilities({
            'platformVersion': settings.ios_platform_version,
            'deviceName': settings.ios_device_name,

            'app': 'bs://sample.ios.app',  # Заменить на свое iOS-приложение

            'bstack:options': {
                'projectName': 'Python Mobile Project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'iOS Test Session',
                'userName': settings.bstack_username,
                'accessKey': settings.bstack_access_key,
            }
        })
    else:
        raise ValueError(f"Unsupported platform: {platform}. Use 'android' or 'ios'")

    with allure.step(f'Init {platform} app session'):
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

    with allure.step('Attach video session'):
        utils.allure.attach_bstack_video(session_id)

"""
Тут можно добавить логику для запуска видео сессии на BStack, если тест провалился/завершился
"""
    # if config.settings.run_on_bstack:
    #   with allure.step('Attach video session'):
    #       utils.allure.attach_bstack_video(session_id)

    # if config.settings.run_on_bstack and request.node.result_of_call.failed:
    #       """
    #       request.node is an "item" because we use the default function scope
    #       """
    #       with allure.step('Take screenshot'):
    #         utils.allure.attach_screenshot(browser)

    #      with allure.step('Save xml report'):
    #      utils.allure.attach_xml(browser)

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item: Item, call: CallInfo):  # noqa
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     result_of_ = outcome.get_result()
#
#     # set a report attribute for each phase of a call, which can
#     # be "setup", "call", "teardown"
#     setattr(item, 'result_of', result_of_.when, result_of_)