Feature: checkout one product
  Scenario: login
    Given in login page
    When enter valid username and password
    And click button login
    Then success login
  Scenario: checkout one product
    Given there is first product
    When click button add to cart on first product
    Then first product is added in cart and counter
    And go to cart and click button checkout
    And enter valid information and click button continue
    And redirect to checkout overview
    When click button finish
    Then success checkout first product
