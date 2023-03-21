from selenium.webdriver.common.by import By

class ChangePasswordLocatorFields:
  password_field = (By.ID, "input-password")
  confirm_password_field = (By.ID, "input-confirm")
  continue_button = (By.XPATH, "//div[@id='content']//input[@value='Continue']")
  confirmation_error_message = (By.CSS_SELECTOR, "#content .text-danger")
