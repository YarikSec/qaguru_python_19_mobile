import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

@allure.title('Android Wiki Search Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Поиск в приложении Wikipedia на Android')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия мобильное приложение Android')
@allure.feature('Поиск с главной страницы')
@allure.story('Поиск по слову Appium')
def test_search():

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.title('Android Wiki Article Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Поиск и открытие статьи в приложении Wikipedia на Android')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия мобильное приложение Android')
@allure.feature('Поиск с главной страницы')
@allure.story('Поиск по слову Appium и клик на первый результат')
def test_search_and_click():

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Click on the first search result'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))
        results.first.click()