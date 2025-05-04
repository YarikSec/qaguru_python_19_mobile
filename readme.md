# Мобильное тестирование с BrowserStack

## Выполненные задачи

- [x] Зарегистрирован аккаунт в https://browserstack.com
- [x] Запущен автотест из занятия локально
- [x] Разработан ещё один автотест на открытие статьи
- [x] Адаптирован conftest.py для работы с двумя типами платформ (Android, iOS)
- [x] Разработан автотест на iOS
- [x] Выполнен вынос данных в .env с использованием pydantic
- [x] Настроена сборка в Jenkins


## Требования

- Python 3.9+
- Poetry
- Установленные зависимости проекта

## Установка

```bash
# Установка Poetry (если не установлен)
curl -sSL https://install.python-poetry.org | python3 -

# Установка зависимостей
poetry install
```

## Настройка

1. Создайте файл `.env` в корне проекта со следующими параметрами:

```
# BrowserStack credentials
BSTACK_USERNAME=your_username
BSTACK_ACCESS_KEY=your_access_key

# Android settings
ANDROID_DEVICE_NAME=Google Pixel 3
ANDROID_PLATFORM_VERSION=9.0

# iOS settings
IOS_DEVICE_NAME=iPhone 14
IOS_PLATFORM_VERSION=16.0

# Common settings
TIMEOUT=10.0
BROWSERSTACK_URL=http://hub.browserstack.com/wd/hub
```

## Запуск тестов

### Запуск Android тестов

```bash
python -m pytest tests/android_app/test_wikipedia.py --platform=android -v
```

### Запуск iOS тестов

```bash
python -m pytest tests/ios_app/test_wikipedia_ios.py --platform=ios -v
```

### Запуск с генерацией Allure-отчета

```bash
python -m pytest tests/android_app/test_wikipedia.py --platform=android --alluredir=./allure-results
python -m pytest tests/ios_app/test_wikipedia_ios.py --platform=ios --alluredir=./allure-results

# Просмотр отчета
allure serve ./allure-results
```

## Структура проекта

- `tests/` - директория с тестами
  - `android_app/` - тесты для Android-приложения
  - `ios_app/` - тесты для iOS-приложения
  - `conftest.py` - общие фикстуры для тестов
- `config.py` - конфигурация проекта с использованием pydantic
- `selene_in_action/` - утилиты для работы с selene и allure