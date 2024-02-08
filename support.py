# -------------------------------------------- Imports --------------------------------------------
import time
import json
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def setup_selenium():

    # ------------------- Selenium Boiler Plate -------------------
    # Setting webdriver options and then creating a session
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    return driver


def close_selenium(driver):
    driver.quit()


def fetch_website(driver, desired_website):

    # Fetching a website
    driver.get(desired_website)


def getlink(driver, linktext: str):

    # Clicking on a link
    exercise_link = driver.find_element(By.LINK_TEXT, linktext)
    exercise_link.click()
    time.sleep(1)


def selenium1create(driver, quantity: int):
    # Creating buttons (0.1 sec delay on each to facilitate progress).
    create_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add Element')]")

    for i in range(0, quantity):
        create_button.click()
        time.sleep(0.1)


def selenium1delete(driver):

    # Finding all created buttons:
    # Deleting one button;
    all_created_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

    # Iterating through created buttons

    for btn in all_created_buttons:
        btn_index = all_created_buttons.index(btn)

        if btn_index % 2 == 0:
            btn.click()
            # print("Deleted Button number " + str(btn_index) + "!") # Some fun checking
            time.sleep(0.1)


def fetch_variables():

    filecheck = os.path.isfile("config/data.json")

    if not filecheck:
        print("Arquivo não encontrado! Favor recadastre-se.")
        login = input("Insira o e-mail de login: ")
        password = input("Insira a senha: ")
        website1 = input("Insira o site-base: ")
        website2 = input("Insira o site-suporte (página de abrir processos): ")
        data = {'login': login, 'senha': password, 'site1': website1, 'site2': website2}

        with open('config/data.json', 'w') as f:
            json.dump(data, f)

    with open("config/data.json", 'r+') as jsonfile:
        json_contents = jsonfile.read()

    json_data = json.loads(json_contents)
    return json_data['login'], json_data['senha'], json_data['site1'], json_data['site2']



