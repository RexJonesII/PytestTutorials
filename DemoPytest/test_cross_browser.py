from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("driver_initialization")
class BaseClass:
  pass

class TestSeleniumGrid(BaseClass):
  def test_lambdatest_remaining_checkboxes(self):
    driver = webdriver.Chrome()
    driver.get("https://lambdatest.github.io/sample-todo-app/")
    driver.find_element(By.XPATH, "//input[@name='li3']").click()
    remaining_checkboxes = driver.find_element\
      (By.CSS_SELECTOR, "span.ng-binding").text
    assert remaining_checkboxes == "4 of 5 remaining"
