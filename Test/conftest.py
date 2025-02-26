import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com")
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
        driver.implicitly_wait(10)
    yield driver
    time.sleep(5)
    driver.quit()


