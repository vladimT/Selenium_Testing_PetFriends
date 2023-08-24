from settings import valid_email, valid_password
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   # Вводим email
   driver.find_element(By.ID, 'email').send_keys(valid_email)
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

   # Проверяем, что список моих питомцев не пустой
   driver.implicitly_wait(10)
   driver.get('https://petfriends.skillfactory.ru/my_pets')

   pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr')
   assert len(pets) > 0, 'нужно добавить питомцев'

   yield driver

   driver.quit()







