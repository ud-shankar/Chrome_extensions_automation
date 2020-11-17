import time
import pytest
from pytest_bdd import given, when, then, parsers, scenario
from Drivers.chromedriver import driver


@scenario("../Feature/Chrome_extensions.feature", "Test one of the feature of the extension - Google Dictionary")
def test_popup():
    pass


@scenario("../Feature/Chrome_extensions.feature", "Test the options page of the extension - Google Dictionary")
def test_options():
    pass


@given("User adds the extension and opens the browser")
def initializing():
    pass                #Chrome driver initialization and other settings are done in driver folder


@when("User opens new tab")
def new_tab():
    driver.execute_script("window.open('');")
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])



@when(parsers.parse("User navigates to the {page} of the extension"))
def pages(page):
    if page == "popup page":
        driver.get("chrome-extension://mgijmajocgfcbeboacabfgobmjgjcoja/browser_action.html")               #Copy the path to your popup html file
    else:
        driver.get("chrome-extension://mgijmajocgfcbeboacabfgobmjgjcoja/options.html")                      #Copy path to your options .html file


@when("User enter word and search for the definition")
def search():
    driver.find_element_by_id("query-field").send_keys("automation")
    driver.find_element_by_id("define-btn").click()
    time.sleep(3)


@then("User verify the definititon is found and close the browser")
def conclude():
    result = driver.find_element_by_class_name("headword").text
    print("Defination for" + result)


@when("User modify the languages setting of the extension")
def modify_options():
    driver.find_element_by_id("language-selector").click()
    driver.find_element_by_xpath("//option[contains(.,'Russian')]").click()
    driver.find_element_by_id("save-btn").click()


@pytest.fixture(scope="session", autouse=True)
def posttest(request):
    yield driver
    driver.quit()