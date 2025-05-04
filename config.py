from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    # BrowserStack credentials
    bstack_username: str = Field(..., env='BSTACK_USERNAME')
    bstack_access_key: str = Field(..., env='BSTACK_ACCESS_KEY')
    app: str = Field(..., env='APP')
    
    # Android specific settings
    android_device_name: str = Field('Google Pixel 3', env='ANDROID_DEVICE_NAME')
    android_platform_version: str = Field('9.0', env='ANDROID_PLATFORM_VERSION')
    
    # iOS specific settings
    ios_device_name: str = Field('iPhone 14', env='IOS_DEVICE_NAME')
    ios_platform_version: str = Field('16.0', env='IOS_PLATFORM_VERSION')
    
    # Common settings
    timeout: float = Field(10.0, env='TIMEOUT')
    browserstack_url: str = Field('http://hub.browserstack.com/wd/hub', env='BROWSERSTACK_URL')
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()