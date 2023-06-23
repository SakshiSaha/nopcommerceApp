from selenium import webdriver
import pytest
import pytest_metadata


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata={
        "Tester": "Sakshi",
        "Project Name": "nop Commerce",
        "Module Name": "Customers",
    }

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

