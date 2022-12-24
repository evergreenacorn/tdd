from selenium import webdriver
from selenium.common import WebDriverException
import unittest
import os

# cur_dir = os.path.join(os.getcwd(), 'app')
# geckodriver_path = os.path.join(cur_dir, 'geckodriver', 'geckodriver')
# host = "localhost"
# port  = "8000"


# # browser = webdriver.Firefox(executable_path=geckodriver_path)

# try:
#   with webdriver.Firefox() as browser:
#     browser.get("http://{}:{}".format(host, port))
#     assert "Congratulations!" in browser.title
#     assert "To-Do" in browser.title, f"Browser title was {browser.title}" 
# except WebDriverException:
#   print("Could not connect to https://{}:{}".format(host, port))


class NewVisitorTest(unittest.TestCase):
  """Тест нового посетителя"""

  def setUp(self):
    """Установка"""
    self.browser = webdriver.Firefox()


  def test_can_start_a_list_and_retrieve_it_later(self):
    """Тест: можно начать список и получить его позже"""
    # Заходим на домашнюю страницу
    self.browser.get("http://localhost:8000")

    # Видим, что заголовок и шапка страницы говорят о
    # списках неотложных дел
    self.assertIn("To-Do", self.browser.title)
    # self.fail("Закончить тест!")

  def tearDown(self):
    """Демонтирование"""
    self.browser.quit()


if __name__ == "__main__":
  unittest.main(warnings="ignore")
