Feature: select low to high price
  Scenario: login
    Given in login page
    When enter valid username and password
    And click button login
    Then success login
  Scenario: select low to high price
    Given there is first product
    When  select low to high price
    Then lowest price is in first list
