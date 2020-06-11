import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox driver")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project_name'] = 'Orange HRM Project'
    config._metadata['Module_name'] = 'Login'
    config._metadata['Tester'] = 'Shalini'

def pytest_metadata(metadata):
    metadata.pop('Packages',None)
    metadata.pop('Plugins',None)