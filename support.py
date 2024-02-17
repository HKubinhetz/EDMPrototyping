# This file contains several support functions to facilitate execution
# and code readability.

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
    # Fetches a website using a selected webdriver
    driver.get(desired_website)


def getlink(driver, linktext: str):
    # Clicks on a link and waits for a second
    exercise_link = driver.find_element(By.LINK_TEXT, linktext)
    exercise_link.click()
    time.sleep(1)


def fetch_login(path):
    # This function fetches all needed variables from the config file;
    # If file doesn't exist, it prompts the user to fill needed info.
    filecheck = os.path.isfile(path + "/config/logindata.json")

    if not filecheck:
        # If file doesn't exist, the user is prompted to provide.
        # The information is then saved for future uses and returned for caller.
        data = userinterface.run_form()
        with open(path + "/config/logindata.json", 'w') as jsonfile:
            json.dump(data, jsonfile)
            return data

    else:
        # If the file exists, data is fetched and returned.
        with open(path + "/config/logindata.json", 'r+') as jsonfile:
            json_contents = jsonfile.read()
            json_data = json.loads(json_contents)
            return json_data  # json_data['login'], json_data['senha']


def get_website_info(path=None, platform=None):
    # Fetches the correct links for an automation,
    # according to "Platform" parameter.

    if platform == "BPM":
        # If platform is 'BPM', opens the bpm.json file and returns its contents.
        with open(path + "/config/bpm.json", 'r+') as jsonfile:
            json_contents = jsonfile.read()

        json_data = json.loads(json_contents)
        return json_data  # json_data['bpm_link1'], json_data['bpm_link1']


def save_cookies(path, cookies):
    with open(path + "/config/cookies.json", 'w') as file:
        json.dump(cookies, file)


def validate_cookies(path):
    # Defines if cookies are valid by checking if there was a recent execution.
    # The current time is recorded on a json file and used for this endeavor.
    # Returns <True> if cookies are still fresh (max 15 minutes old);
    # Returns <False> otherwise.

    filecheck = os.path.isfile(path + "/config/lastrun.json")
    timedelta = 0

    if filecheck:
        # If file exists, calculations are made and the new time is saved.
        with open(path + "/config/lastrun.json", 'r+') as jsonfile:

            # Part 1 - Read file and calculate time since last execution
            json_contents = jsonfile.read()
            json_data = json.loads(json_contents)
            lastrun = json_data['lastrun']
            timedelta = time.time() - lastrun

            # Part 2 - Clear file contents and record current time
            jsonfile.seek(0)
            jsonfile.truncate()
            data = {'lastrun': time.time()}
            json.dump(data, jsonfile)

            # Cookie is valid for 900 seconds, or 15 minutes.
            if timedelta < 900:
                return True
            else:
                return False

    if not filecheck:
        # If file doesn't exist, creates a new one.
        # Current time is recorded and function returns <False> to its caller.

        data = {'lastrun': time.time()}
        with open(path + "/config/lastrun.json", 'w') as jsonfile:
            json.dump(data, jsonfile)
        return False


