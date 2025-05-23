from behave import given, when, then
from pages.login_page import LoginPage
from utils.json_utils import read_json_data, write_test_results

@given("the browser is launched")
def step_launch_browser(context):
    from selenium import webdriver
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)

@when("user attempts login with multiple credentials from JSON")
def step_login_multiple(context):
    context.results = []
    data = read_json_data("D:\Automation\PAT-EB-6\Behave_Excel_Demo\\features\data\credentials.json")
    for cred in data:
        username = cred['username']
        password = cred['password']
        context.login_page.login(username, password)
        status = context.login_page.login_successful()
        cred["result"] = "success" if status else "failure"
        context.results.append(cred)
        context.driver.get("https://www.saucedemo.com/")

@then("update the test result into JSON file")
def step_write_result(context):
    write_test_results("features/data/credentials.json", context.results)
    context.driver.quit()
