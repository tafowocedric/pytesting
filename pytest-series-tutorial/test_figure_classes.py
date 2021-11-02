from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver

    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver

    yield
    ff_driver.close()


@pytest.mark.usefixtures('init_chrome_driver')
class BaseChromeTest:
    pass


@pytest.mark.usefixtures('init_chrome_driver')
class TestGoogleChrome(BaseChromeTest):
    def test_google_title_chrome(self):
        self.driver.get('https://www.google.com')

        assert self.driver.title == "Google"


@pytest.mark.usefixtures('init_ff_driver')
class BaseFireFoxTest:
    pass


@pytest.mark.usefixtures('init_ff_driver')
class TestFireFoxChrome(BaseFireFoxTest):
    def test_google_title_chrome(self):
        self.driver.get('https://www.google.com')

        assert self.driver.title == "Google"
