import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from utilities.test_data import TestData

@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
  if request.param == "chrome":
    driver = webdriver.Chrome()
  elif request.param == "firefox":
    driver = webdriver.Firefox()
  elif request.param == "edge":
    driver = webdriver.Edge()
  request.cls.driver = driver
  print("Browser: ", request.param)
  driver.get(TestData.url)
  driver.maximize_window()
  yield
  print("Close Driver")
  driver.close()

# 1st Step: Declare Variables For Setting Up LambdaTest
user_name = "Rex.Jones"
access_token = "YxU1eSK0Cx3WkN7d2FouJ4agNhPUiw8yOrXWAF8TN19LvOueVB"
remote_url = "https://" + user_name + ":" + access_token + "@hub.lambdatest.com/wd/hub"

# 2nd Step: Define The Desired Capabilities (3 Caps)
chrome_caps = {
  "build"       : "1.0",
  "name"        : "LambdaTest Grid On Chrome",
  "platform"    : "Windows 10",
  "browserName" : "Chrome",
  "version"     : "latest"
  }

firefox_caps = {
  "build"         : "2.0",
  "name"          : "LambdaTest Grid On Firefox",
  "platform"      : "Windows 10",
  "browserName"   : "Firefox",
  "version"       : "latest"
}

edge_caps = {
  "build"         : "3.0",
  "name"          : "LambdaTest Grid On Edge",
  "platform"      : "Windows 10",
  "browserName"   : "Edge",
  "version"       : "latest"
}

#3rd Step: Connect To LambdaTest Using A Fixture & RemoteConnection
@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver_initialization(request):
  """
  Initialize Driver For Selenium Grid On LambdaTest
  :param request:
  """
  desired_caps = {}

  if request.param == "chrome":
    desired_caps.update(chrome_caps)
    driver = webdriver.Remote(
      command_executor=RemoteConnection(remote_url),
      desired_capabilities={"LT:Options":desired_caps})
  elif request.param == "firefox":
    desired_caps.update(firefox_caps)
    driver = webdriver.Remote(
      command_executor=RemoteConnection(remote_url),
      desired_capabilities={"LT:Options": desired_caps})
  elif request.param == "edge":
    desired_caps.update(edge_caps)
    driver = webdriver.Remote(
      command_executor=RemoteConnection(remote_url),
      desired_capabilities={"LT:Options": desired_caps})
  request.cls.driver = driver
  yield
  driver.close()
