from selenium import webdriver
from selenium.webdriver.common.by import By

def test_5_open():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    ## Поиск элемента
    username = driver.find_element(By.CSS_SELECTOR, '[id="user-name"]')
    if username is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')

    password = driver.find_element(By.CSS_SELECTOR, '#password')

    if password is None:
        print('Элемент password не найден')
    else:
        print('Элемент password найден')

    submit = driver.find_element(By.CSS_SELECTOR, '[class="submit-button btn_action"]')

    if submit is None:
        print('Элемент submit не найден')
    else:
        print('Элемент submit найден')
