import pytest
import importlib
import datetime
from selenium_library import Base
from selenium import webdriver

pytest_plugins = [
    'lib.plugins.configuration',
]

## can be implemented when running tests on a CI pipeline
@pytest.fixture(scope='session')
def selenium_grid(configuration):
    return configuration.get('SELENIUM_GRID')


@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.close()



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True, scope='function')
def get_screenshot_on_test_failure(request):
    driver = webdriver.Chrome()
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        name = request.node.nodeid.translate(str.maketrans('/:', '--')) + '.png'
        if request.config.option.screenshots_dir_path is not None:
            driver.save_screenshot(name,
                                                  screenshot_dir=request.config.option.screenshots_dir_path)
        else:
            driver.save_screenshot(name)


