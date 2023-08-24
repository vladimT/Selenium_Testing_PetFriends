import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_have_all_pets(driver):
    '''Проверяем что на странице со списком моих питомцев количество питомцев (заведенных карточек) соответствует показателю статистике'''
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    # Находим и сохраняем данные по статистике (количество питомцев)
    statistic = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@class=".col-sm-4 left"]')))

    # Получаем число из статистики
    number = statistic.text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Определяем и сохраняем локатор карточек питомцев
    pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr')

    driver.implicitly_wait(10)

    # Получаем количество карточек питомцев
    pets = len(pets)

    # Сравниваем показатель статистики с количеством карточек питомцев
    assert number == pets

def test_pets_photo(driver):
    '''Проверим, что на странице со списком моих питомцев хотя бы у половины из них есть фото'''
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    # Определим локатор фотографии питомцев и количество питомцев с фото
    photo = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    pets_photo = 0
    for i in range(len(photo)):
        if photo[i].get_attribute('src') != '':
            pets_photo += 1

    # Находим и сохраняем данные по статистике (количество питомцев)
    statistic = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@class=".col-sm-4 left"]')))

    # Получаем число из статистики
    number = statistic.text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # С помощью статистики проверяем, что как минимум у половины питомцев есть фото
    assert number/2 <= pets_photo

def test_pets_have_age_name_type(driver):
    '''Проверим, что на странице со списком моих питомцев у всех есть имя, возраст и порода'''
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    # Определим локатор строки с указанием данных об имени, возрасте и породе питомцев
    pets = driver.find_elements(By.XPATH, '//tbody/tr')

    # В полученном массиве проверим, что все 3 составляющие (имя, порода, возраст) - не пустые
    for i in range(len(pets)):
        data_pet = pets[i].text.replace('\n', '').replace('×', '')
        split_pet = data_pet.split(' ')
        result = len(split_pet)
        assert result == 3

def test_different_names(driver):
    '''Проверим, что на странице со списком моих питомцев у всех питомцев разные имена'''
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    # Определим локатор имени питомцев и сохраним имена в список
    pets_names = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

    names = []
    for i in range(len(pets_names)):
        name = pets_names[i].text
        name = name.split("\n")[0]
        names.append(name)

    # Создадим множество с уникальными именами
    unique_names = list(set(names))

    # Сверяем число имен из списка с числом уникальных имен из множества
    assert len(names) == len(unique_names)

def test_different_pets(driver):
    '''Проверим, что на странице со списком моих питомцев нет одинаковых питомцев'''
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    # Определяем и сохраняем локатор карточек питомцев
    pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr')

    # Сохраним имена, породы и возраст питомцев в список
    data_pets = []
    for i in range(len(pets)):
        data = pets[i].text
        data = data.split("\n")[0]
        data_pets.append(data)

    # Создадим множество с уникальными именами, породами и возрастами питомцев
        unique_pets = list(set(data_pets))

    # Сверяем число имен, пород и возрастов из списка с числом уникальных имен, пород и возрастов из множества
        assert len(data_pets) == len(unique_pets)




