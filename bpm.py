# ------------------------------------------------ IMPORTS ------------------------------------------------
import time
import json
import support as sp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


# ------------------------------------------------ VARIABLES ------------------------------------------------
email = sp.fetch_variables()[0]
password = sp.fetch_variables()[1]
website = sp.fetch_variables()[2]
website2 = sp.fetch_variables()[3]

# ---------------------------------------------- AUX FUNCTIONS ----------------------------------------------


def button_advance(driver):
    login_advance_button = WebDriverWait(driver, 120).until(ec.visibility_of_element_located((By.ID, "idSIButton9")))
    time.sleep(0.25)
    login_advance_button.click()


def load_cookies():
    # Load cookies to a variable from a file
    with open('config/cookies.json', 'r') as file:
        cookies = json.load(file)

    # Navigating to correct link
    chrome_driver = sp.setup_selenium()
    chrome_driver.maximize_window()
    sp.fetch_website(chrome_driver, website2)

    # Set stored cookies to maintain the session
    for cookie in cookies:
        chrome_driver.add_cookie(cookie)

    chrome_driver.refresh()

    # Check Logged In status
    WebDriverWait(chrome_driver, 30).until(ec.visibility_of_element_located((By.ID, "topo")))
    print("Logado!")

    return chrome_driver


def open_bpm_ticket(chrome_driver):
    ticket_button = chrome_driver.find_element(By.LINK_TEXT, "Abertura de Chamados para Medição")
    ticket_button.click()
    form_frame = WebDriverWait(chrome_driver, 60).until(ec.presence_of_element_located((By.ID, "form-app")))
    chrome_driver.switch_to.frame(form_frame)


# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------------ EXECUTION ------------------------------------------------
# -----------------------------------------------------------------------------------------------------------


# --------------------------------------------- PART 1 - LOGIN ----------------------------------------------

def login_user():
    # Navigating to correct link
    chrome_driver = sp.setup_selenium()
    sp.fetch_website(chrome_driver, website)

    # Login Button
    login_button = WebDriverWait(chrome_driver, 10).\
        until(ec.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[3]/div/span")))
    login_button.click()

    # Login Field
    login_field = WebDriverWait(chrome_driver, 10).\
        until(ec.visibility_of_element_located((By.ID, "i0116")))
    login_field.send_keys(email)

    # Login Advance
    button_advance(chrome_driver)

    # Password Field
    password_field = WebDriverWait(chrome_driver, 10).\
        until(ec.visibility_of_element_located((By.ID, "i0118")))

    password_field.send_keys(password)

    # Login Advance - Part 2
    button_advance(chrome_driver)

    # Keep Logged In
    # Login Advance - Part 2
    button_advance(chrome_driver)

    # Check Logged In status
    logged_in = WebDriverWait(chrome_driver, 120).\
        until(ec.visibility_of_element_located((By.ID, "topo")))
    print("Logado!")

    # Get and store cookies after login
    cookies = chrome_driver.get_cookies()

    # Store cookies in a file
    with open('config/cookies.json', 'w') as file:
        json.dump(cookies, file)

# --------------------------------------------- PART 2 - TICKET ----------------------------------------------


# Also waits for page to finish loading

def build_bpm_ticket(chrome_driver):
    cdie_field = WebDriverWait(chrome_driver, 300).\
        until(ec.presence_of_element_located((By.XPATH, "//*[@id='COD_INSTALACAO']")))
    time.sleep(4)
    cdie_field.click()
    cdie_field.send_keys("000000")
    cdie_field.send_keys(Keys.TAB)

    # ---------------------------------- JavaScript Alert ----------------------------------
    # Wait for the alert to be displayed and store it in a variable
    alert = WebDriverWait(chrome_driver, 10).until(ec.alert_is_present())
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
    client_name = chrome_driver.find_element(By.ID, "CLIENTE")
    client_name.send_keys("CLIENTE TESTE")

    # ---------------------------------- Fourth Field - Region ----------------------------------

    region_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID, "REGIAO_caret")))
    ActionChains(chrome_driver).move_to_element(region_caret)
    region_caret.click()
    region_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID, "REGIAO__search")))
    region_search.click()
    region_search.send_keys("RMSP")
    region_search.send_keys(Keys.ENTER)

    # ---------------------------------- Fifth Field - City ----------------------------------

    city_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID, "MUNICIPIO_caret")))
    city_caret.click()
    ActionChains(chrome_driver).move_to_element(city_caret)
    city_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID, "MUNICIPIO__search")))
    city_search.click()
    # time.sleep(2)
    city_search.send_keys("SAO PAULO")
    city_search.send_keys(Keys.ENTER)

    # ---------------------------------- Sixth Field - Object ----------------------------------

    object_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID, "OBJETO_caret")))
    object_caret.click()
    ActionChains(chrome_driver).move_to_element(object_caret)
    object_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID, "OBJETO__search")))
    object_search.click()
    object_search.send_keys("Faturamento")
    object_search.send_keys(Keys.ENTER)

    # ---------------------------------- Seventh Field - Problem ----------------------------------
    problem_caret = WebDriverWait(chrome_driver, 10).until(ec.presence_of_element_located((By.ID,
                                                                                           "CARACTERISTICA_caret")))
    problem_caret.click()
    problem_search = WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable((By.ID,
                                                                                        "CARACTERISTICA__search")))
    problem_search.click()
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
    description_field.send_keys("Prezados, bom dia! Poderiam por gentileza estimar o cliente XXX - YYY? Motivo: ZZZ. "
                                "Obrigado e um ótimo dia!")

    # ---------------------------------- FINAL DATA ACQUISITION ----------------------------------

    final_button = chrome_driver.find_element(By.ID, "aprovar")
    print(final_button.text)
