from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
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
    header_text = self.browser.find_element(
      by=By.TAG_NAME,
      value="h1"
    ).text
    self.assertIn("To-Do", header_text)

    # Предлагается ввести элемент списка
    inputbox = self.browser.find_element(
      by=By.ID,
      value="id_new_item"
    )
    self.assertEqual(
      inputbox.get_attribute("placeholder"),
      "Enter a to-do item"
    )

    # Набираем в текстовом поле "Купить павлиньи перья"
    inputbox.send_keys("Купить павлиньи перья")

    # Когда мы нажимаем enter, страница обновляется, и теперь
    # страница содержит "1: Купить павлиньи перья" в качестве
    # элемента списка
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    table = self.browser.find_element(
      by=By.ID,
      value="id_list_table"
    )
    rows = table.find_elements(
      by=By.TAG_NAME,
      value="tr"
    )
    self.assertTrue(
      any(
        row.text == "1: Купить павлиньи перья"\
          for row in rows
      )
    )

    # Текстовое поле по-прежнему приглашает добавить еще
    # один элемент.
    # Вводим: "Сделать мушку из павлиных перьев"
    self.fail("Закончить тест!")

  def tearDown(self):
    """Демонтирование"""
    self.browser.quit()


if __name__ == "__main__":
  unittest.main(warnings="ignore")
