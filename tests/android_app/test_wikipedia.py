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

@allure.title('Android Wiki Onboarding Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Тестирование страницы "Getting Started" в приложении Wikipedia на Android')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия мобильное приложение Android')
@allure.feature('Тестирование страницы "Getting Started"')
@allure.story('Тестирование страницы "Getting Started"')
def test_getting_started():

    with ((step('Open second page'))):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('New ways to explore'))

    with ((step('Open third page'))):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Reading lists with sync'))

    with ((step('Open fourth page'))):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Data & Privacy'))

    with ((step('Click get started'))):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')
                        ).should(have.text('Wikipedia games'))

@allure.title('Android Wiki Reading List Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Тестирование создания и удаления списка чтения в приложении Wikipedia на Android')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия мобильное приложение Android')
@allure.feature('Тестирование создания и удаления списка чтения')
@allure.story('Тестирование создания и удаления списка чтения')
def test_reading_list():
    if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')
                        ).should(have.text('Wikipedia games')):
        with ((step('Click on the reading list'))):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')
                            ).click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/reading_list_item_title')
                            ).should(have.text('Reading list'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')
                            ).should(have.text('Reading list'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button')).click()

            with ((step('Click on the delete'))):
                if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_delete')).should(have.text('Delete')):
                    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_delete')).click()
                    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/reading_list_item_title')
                                    ).should(have.text('Reading list'))
                    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')
                                    ).should(have.text('Reading list'))

@allure.title('Android Wiki Favorites Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Тестирование добавления и удаления из избранного в приложении Wikipedia на Android')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия мобильное приложение Android')
@allure.feature('Тестирование добавления и удаления из избранного')
@allure.story('Тестирование добавления и удаления из избранного')
def test_favorites():
    pass