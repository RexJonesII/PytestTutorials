from selenium.webdriver.common.by import By


class BasePage:
  """
  The Purpose Of A BasePage Is To Contain Methods Common To All Page Objects
  """
  def __init__(self, driver):
    self.driver = driver

  def find(self, *locator):
    return self.driver.find_element(*locator)

  def click(self, locator):
    self.find(*locator).click()
    # self.driver.find_element(*locator).click()

  def set(self, locator, value):
    self.find(*locator).clear()
    self.find(*locator).send_keys(value)

  def get_text(self, locator):
    return self.find(*locator).text

  def get_title(self):
    return self.driver.title

  def click_right_menu_page(self, page_name):
    # self.click(self.page(page_name))
    page = By.XPATH, "//aside[@id='column-right']//a[text()=' "+ page_name +"']"
    self.click(page)

  # Below Method Allows Us To Click Page, Check If Page Is Visible, & More Actions
  def page(self, page_name):
    return By.XPATH, "//aside[@id='column-right']//a[text()=' "+ page_name +"']"
