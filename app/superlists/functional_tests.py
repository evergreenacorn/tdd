from selenium import webdriver
from selenium.common import WebDriverException
import os

cur_dir = os.path.join(os.getcwd(), 'app')
geckodriver_path = os.path.join(cur_dir, 'geckodriver', 'geckodriver')
host = "localhost"
port  = "8000"


# browser = webdriver.Firefox(executable_path=geckodriver_path)

try:
  with webdriver.Firefox() as browser:
    browser.get("http://{}:{}".format(host, port))
    assert "Congratulations!" in browser.title
except WebDriverException:
  print("Could not connect to https://{}:{}".format(host, port))
