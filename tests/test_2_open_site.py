from selenium import webdriver
from selenium.webdriver.common.by import By

def test_2_open():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")

    ## Поиск элемента
    icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
    if icon is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    if password is None:
        print('Элемент password не найден')
    else:
        print('Элемент password найден')

