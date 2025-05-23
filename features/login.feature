Feature: Login functionality of SauceDemo

  Scenario: Login with multiple credentials from JSON
    Given the browser is launched
    When user attempts login with multiple credentials from JSON
    Then update the test result into JSON file
