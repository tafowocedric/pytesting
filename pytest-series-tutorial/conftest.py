import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class', params=["chrome", "firefox"])
def init_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = driver
    driver.implicitly_wait(10)

    yield
    driver.close()
