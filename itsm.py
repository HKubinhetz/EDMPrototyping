# ------------------------------------------------ IMPORTS ------------------------------------------------
import os
import time
import json
import support as sp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# ------------------------------------------------- PATH ---------------------------------------------------

mypath = os.path.dirname(__file__)

# ------------------------------------------------ VARIABLES ------------------------------------------------

login_variables = sp.fetch_login(mypath)
email = login_variables["login"]
password = login_variables["senha"]

# TODO - Build a JSON configuration file that enables user to change one or two parameters (like password)
#  (maybe that other task where you read existing data from the file can help you here)

# ------------------------------------------------ VARIABLES ------------------------------------------------

itsm_link = "https://comgas.service-now.com/comgas_itsm?id=sc_cat_item&sys_id=29f7a3bb1b027890fa2442ece54bcb5a"


# ---------------------------------------------- AUX FUNCTIONS ----------------------------------------------
# Todo - Minimize repetition, bring scalability
# Todo - Read better jsons to enable several websites in the same file
def button_advance(driver):
    login_advance_button = WebDriverWait(driver, 120).until(ec.visibility_of_element_located((By.ID, "idSIButton9")))
    time.sleep(0.25)
    login_advance_button.click()


def load_cookies(driver):
    chrome_driver = driver

    # Navigating to correct link
    sp.fetch_website(chrome_driver, itsm_link)

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

# --------------------------------------------- PART 1 - LOGIN ----------------------------------------------


def login_user():
    valid_cookies = sp.validate_cookies(mypath)

    # Navigating to homepage
    chrome_driver = sp.setup_selenium()
    sp.fetch_website(chrome_driver, itsm_link)
    chrome_driver.maximize_window()

    if not valid_cookies:
        # If cookies ARE NOT valid, create them:
        # Login Button
        # login_button = WebDriverWait(chrome_driver, 10). \
        #    until(ec.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[3]/div/span")))
        # login_button.click()

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
        # logged_in = WebDriverWait(chrome_driver, 120). \
        #    until(ec.visibility_of_element_located((By.ID, "topo")))
        # print("BPM - Login Success!")

        # Get and store cookies after login
        cookies = chrome_driver.get_cookies()
        sp.save_cookies(mypath, cookies)
        # Redirecting to correct link
        sp.fetch_website(chrome_driver, itsm_link)
        return chrome_driver

    else:
        # If cookies ARE valid, load them.
        load_cookies(chrome_driver)
        return chrome_driver


login_user()