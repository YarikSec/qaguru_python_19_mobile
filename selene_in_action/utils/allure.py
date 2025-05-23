import allure
from config import settings
from selene import browser


def attach_bstack_video(session_id):
    """
    Прикрепляет видео записи сессии BrowserStack к отчету Allure
    """
    import requests
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(settings.bstack_username, settings.bstack_access_key),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )

def attach_screenshot(browser):
    """
    Прикрепляет скриншот экрана к отчету Allure
    """
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

def attach_xml(browser):
    """
    Прикрепляет дамп XML страницы к отчету Allure
    """
    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )