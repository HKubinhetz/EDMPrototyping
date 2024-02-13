# -------------------------------------------- Imports --------------------------------------------
import time
import json
import os.path
import userinterface
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
    # Quits webdriver
    driver.quit()


def fetch_website(driver, desired_website):
    # Fetches a website
    driver.get(desired_website)


def getlink(driver, linktext: str):
    # Clicks on a link
    exercise_link = driver.find_element(By.LINK_TEXT, linktext)
    exercise_link.click()
    time.sleep(1)


def fetch_variables():
    # This function fetches all needed variables from config file;
    # If file doesn't exist, it prompts the user to fill needed info.
    filecheck = os.path.isfile("config/data.json")

    if not filecheck:

        """ 
        
        >>> Original process:
        
        print("Arquivo não encontrado! Favor recadastre-se.")
        login = input("Insira o e-mail de login: ")
        password = input("Insira a senha: ")
        website1 = input("Insira o site-base: ")
        website2 = input("Insira o site-suporte (página de abrir processos): ")
        data = {'login': login, 'senha': password, 'site1': website1, 'site2': website2}
        
        """

        data = userinterface.run_form()

        with open('config/data.json', 'w') as f:
            json.dump(data, f)

    with open("config/data.json", 'r+') as jsonfile:
        json_contents = jsonfile.read()

    json_data = json.loads(json_contents)
    return json_data['login'], json_data['senha'], json_data['site1'], json_data['site2']



