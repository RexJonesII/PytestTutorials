import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
  pass

class Test_Drivers(BaseClass):
  def test_multiple_browsers(self):
    self.driver.get("https://www.lambdatest.com/selenium-playground/")
    header = self.driver.find_element(By.CSS_SELECTOR,
      "div#__next h1").text
    print("Header: ", header)
    assert header == "Selenium Playground"
