# ------------------------------------------------ IMPORTS ------------------------------------------------
import os
import time
import json
import support as sp
import addressbuilder as ab
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

# ------------------------------------------------- PATH ---------------------------------------------------

mypath = os.path.dirname(__file__)

# ------------------------------------------------ VARIABLES ------------------------------------------------

login_variables = sp.fetch_login(mypath)
email = login_variables["login"]
password = login_variables["senha"]

site_variables = sp.get_website_info(mypath, "BPM")
bpm_link1 = site_variables["bpm_link1"]
bpm_link2 = site_variables["bpm_link2"]


# ---------------------------------------------- AUX FUNCTIONS ----------------------------------------------


def button_advance(driver):
    login_advance_button = WebDriverWait(driver, 120).until(ec.visibility_of_element_located((By.ID, "idSIButton9")))
    time.sleep(0.25)
    login_advance_button.click()


def load_cookies(driver):
    chrome_driver = driver

    # Navigating to correct link
    sp.fetch_website(chrome_driver, bpm_link2)

    # Load cookies to a variable from a file
    with open(mypath + "/config/cookies.json", 'r') as file:
        cookies = json.load(file)

    # Set stored cookies to maintain the session
    for cookie in cookies:
        chrome_driver.add_cookie(cookie)

    chrome_driver.refresh()

    # Check Logged In status
    WebDriverWait(chrome_driver, 30).until(ec.visibility_of_element_located((By.ID, "topo")))
    print("Logado!")

    return chrome_driver


def open_bpm_ticket(chrome_driver):
    ticket_button = (WebDriverWait(chrome_driver, 60)
                     .until(ec.presence_of_element_located((By.LINK_TEXT, "Abertura de Chamados para Medição"))))
    ticket_button.click()
    form_frame = WebDriverWait(chrome_driver, 60).until(ec.presence_of_element_located((By.ID, "form-app")))
    ticket_number = chrome_driver.find_element(By.NAME, "sCodProcesso").get_attribute('value')
    chrome_driver.switch_to.frame(form_frame)
    return ticket_number


def close_bpm_ticket(chrome_driver):
    cancel_button = WebDriverWait(chrome_driver, 60).until(ec.presence_of_element_located((By.ID, "cancel")))
    cancel_button.click()


def kill_driver(chrome_driver):
    chrome_driver.close()


# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------------ EXECUTION ------------------------------------------------
# -----------------------------------------------------------------------------------------------------------


# --------------------------------------------- PART 1 - LOGIN ----------------------------------------------

def login_user():
    valid_cookies = sp.validate_cookies(mypath)

    # Navigating to homepage
    chrome_driver = sp.setup_selenium()
    sp.fetch_website(chrome_driver, bpm_link1)
    chrome_driver.maximize_window()

    if not valid_cookies:
        # If cookies ARE NOT valid, create them:
        # Login Button
        login_button = WebDriverWait(chrome_driver, 10). \
            until(ec.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[3]/div/span")))
        login_button.click()

        # Login Field
        login_field = WebDriverWait(chrome_driver, 10). \
            until(ec.visibility_of_element_located((By.ID, "i0116")))
        login_field.send_keys(email)

        # Login Advance
        button_advance(chrome_driver)

        # Password Field
        password_field = WebDriverWait(chrome_driver, 10). \
            until(ec.visibility_of_element_located((By.ID, "i0118")))

        password_field.send_keys(password)

        # Login Advance - Part 2
        button_advance(chrome_driver)

        # Keep Logged In
        # Login Advance - Part 2
        button_advance(chrome_driver)

        # Check Logged In status
        logged_in = WebDriverWait(chrome_driver, 120). \
            until(ec.visibility_of_element_located((By.ID, "topo")))
        print("BPM - Login Success!")

        # Get and store cookies after login
        cookies = chrome_driver.get_cookies()
        sp.save_cookies(mypath, cookies)
        # Redirecting to correct link
        sp.fetch_website(chrome_driver, bpm_link2)
        return chrome_driver

    else:
        # If cookies ARE valid, load them.
        load_cookies(chrome_driver)
        return chrome_driver


# --------------------------------------------- PART 2 - TICKET ----------------------------------------------

# Also waits for page to finish loading

def build_bpm_ticket(chrome_driver, input_code, input_name, input_reason,
                     model=None, start_date=None, end_date=None, billing_date=None):

    # Fetching Variables
    client_code = int(input_code)
    client_name = str(input_name)
    client_reason = str(input_reason)
    client_info, client_address = ab.get_clientdata(client_code, mypath)
    client_dates = sp.format_dates(start_date, end_date, billing_date)

    cdie_field = WebDriverWait(chrome_driver, 300). \
        until(ec.presence_of_element_located((By.XPATH, "//*[@id='COD_INSTALACAO']")))
    time.sleep(4)
    cdie_field.click()
    cdie_field.send_keys(client_code)
    cdie_field.send_keys(Keys.TAB)

    # ---------------------------------- JavaScript Alert ----------------------------------
    # Wait for the alert to be displayed and store it in a variable
    alert = WebDriverWait(chrome_driver, 300).until(ec.alert_is_present())
    time.sleep(1)
    alert.accept()

    # ---------------------------------- Second Field - Soliciting Sector ----------------------------------
    area_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID,
                                                                                        "AREA_SOLICITANTE_caret")))
    area_caret.click()
    area_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID,
                                                                                     "AREA_SOLICITANTE__search")))
    area_search.click()
    area_search.send_keys("Sala de Controle")
    area_search.send_keys(Keys.ENTER)
    area_search.send_keys(Keys.ESCAPE)

    # ---------------------------------- Third Field - Client Name ----------------------------------
    form_name = chrome_driver.find_element(By.ID, "CLIENTE")
    form_name.send_keys(client_name)

    # ---------------------------------- Fourth Field - Region ----------------------------------

    region_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID, "REGIAO_caret")))
    ActionChains(chrome_driver).move_to_element(region_caret)
    region_caret.click()
    region_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID, "REGIAO__search")))
    region_search.click()

    # Handling client not found error:
    if client_info is None:
        region_search.send_keys('RMSP')
        region_search.send_keys(Keys.ENTER)
    else:
        region_search.send_keys(client_info['region'])
        region_search.send_keys(Keys.ENTER)

    # ---------------------------------- Fifth Field - City ----------------------------------

    city_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID, "MUNICIPIO_caret")))
    city_caret.click()
    ActionChains(chrome_driver).move_to_element(city_caret)
    city_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID, "MUNICIPIO__search")))
    city_search.click()

    # Handling client not found error:
    if client_info is None:
        city_search.send_keys('SAO PAULO')
        city_search.send_keys(Keys.ENTER)
    else:
        city_search.send_keys(client_info['city'])
        city_list = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID, "MUNICIPIO_0")))
        city_list.send_keys(Keys.ENTER)

    # ---------------------------------- Sixth Field - Object ----------------------------------

    object_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID, "OBJETO_caret")))
    object_caret.click()
    ActionChains(chrome_driver).move_to_element(object_caret)
    object_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID, "OBJETO__search")))
    object_search.click()

    if model == "visit":
        object_search.send_keys("Eletroconversor")  # Searching for "Eletroconversor de Volume"
        object_list = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID, "OBJETO_0")))
        object_list.send_keys(Keys.ENTER)
    else:
        object_search.send_keys("Faturamento")
        object_search.send_keys(Keys.ENTER)

    # ---------------------------------- Seventh Field - Problem ----------------------------------
    problem_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID,
                                                                                           "CARACTERISTICA_caret")))
    problem_caret.click()
    problem_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID,
                                                                                        "CARACTERISTICA__search")))
    problem_search.click()

    if model == "visit":
        problem_search.send_keys("Apagado")
        problem_search.send_keys(Keys.ENTER)

    else:
        problem_search.send_keys("Estimar Dados")
        problem_search.send_keys(Keys.ENTER)

    # ---------------------------------- Eighth Field - Billing Problem? ----------------------------------
    billing_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID,
                                                                                           "IDE_PROBLEMA_FATUR_caret")))
    billing_caret.click()
    billing_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID,
                                                                                        "IDE_PROBLEMA_FATUR__search")))
    billing_search.click()
    billing_search.send_keys("Sim")
    billing_search.send_keys(Keys.ENTER)

    # ---------------------------------- Text Field - Full description ----------------------------------
    description_field = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID, "DESCRICAO")))
    description_field.click()

    if client_info is None:
        client_address = "Observação: Dados do cliente não encontrados na base SAP."

    print(model)

    if model == "visit":
        description_field. \
            send_keys(f"Prezados! Poderiam por gentileza verificar o cliente {client_code} - {client_name}? \n"
                      f"Foi solicitada uma visita por conta do seguinte motivo: {client_reason}. \n \n"
                      f"{client_address} \n \n"
                      "Obrigado e um ótimo dia!")

    else:
        description_field. \
            send_keys(f"Prezados! Poderiam por gentileza estimar o cliente {client_code} - {client_name}? \n"
                      f"Motivo: {client_reason}. \n"
                      f"Período de Leitura: {client_dates['start_date']} a {client_dates['end_date']} \n"
                      f"Data de Faturamento: {client_dates['billing_date']} \n \n "
                      "Obrigado e um ótimo dia!")

    # ---------------------------------- FINAL DATA ACQUISITION ----------------------------------

    # Optional Approve button
    # final_button = chrome_driver.find_element(By.ID, "aprovar")
