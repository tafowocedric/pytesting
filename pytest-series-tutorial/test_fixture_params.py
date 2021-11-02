from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(scope='class', params=["chrome", "firefox"])
def init_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = driver

    yield
    driver.close()


@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass


class TestGoogle(BaseTest):
    def test_google_title(self):
        self.driver.get('https://google.com')
        assert self.driver.title == 'Google'
