import allure
import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@pytest.mark.skip('Пропускаем тест - еще в работе')
@allure.title('iOS Wiki Search Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Поиск в приложении Wikipedia на iOS')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия iOS')
@allure.feature('Поиск')
@allure.story('Поиск по слову Appium в iOS приложении')
def test_search_ios():

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.CLASS_NAME, "XCUIElementTypeSearchField")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.CLASS_NAME, 'XCUIElementTypeCell'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@pytest.mark.skip('Пропускаем тест - еще в работе')
@allure.title('iOS Wiki Article Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Поиск и открытие статьи в приложении Wikipedia на iOS')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия iOS')
@allure.feature('Открытие статьи')
@allure.story('Поиск по слову Appium и открытие статьи в iOS приложении')
def test_search_and_open_article_ios():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.CLASS_NAME, "XCUIElementTypeSearchField")).type('Appium')

    with step('Click on the first search result'):
        results = browser.all((AppiumBy.CLASS_NAME, 'XCUIElementTypeCell'))
        results.should(have.size_greater_than(0))
        results.first.click()

    with step('Verify article is opened'):
        article_title = browser.element((AppiumBy.ACCESSIBILITY_ID, "Article title"))
        article_title.should(have.text_containing('Appium')) 