from pydantic import BaseSettings


class TestSettings(BaseSettings):
    service_url = 'http://web:8000'


test_settings = TestSettings()
