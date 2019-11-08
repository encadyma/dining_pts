## A script to authenticate the current user
## with CalNet, given a Selenium Webdriver
## instance.

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCond
from selenium.webdriver.common.by import By

from getpass import getpass

from constants import *

def auth_calnet(driver, username=None, password=None):
    print("""
>> [CALNET LOGIN REQUIRED BEYOND THIS POINT]
   This program has requested to authenticate you into CalNet.
   CalNet is the login system used by students and faculty in UC Berkeley.

   If you have downloaded this program from official sources, this program 
   will not store or deliver your CalNet login to any service other than
   CalNet itself. Please DOUBLE CHECK the script's source code that 
   you are running before trusting your credentials with it.

   This script begins running in `./cal_auth.py`. This Python function is `cal_auth`.
""")

    raw_input("Press ENTER to proceed.")

    if not username:
        username = raw_input("CalNet username: ")
    
    if not password:
        password = getpass("CalNet password (input is hidden): ")

    try:
        driver.get(URL_AUTH_PORTAL)

        try:
            WebDriverWait(driver, 10).until(
                ExpCond.presence_of_element_located((By.ID, "username"))
            )
        except:
            print("The authentication page timed out. Please check your internet connection.")
            return False

        input_uid = driver.find_element_by_id("username")
        input_pass = driver.find_element_by_id("password")

        input_uid.send_keys(username)
        input_pass.send_keys(password)
        input_pass.send_keys(Keys.ENTER)

        print("Logging you in...")

        # Wait until the Duo Security iFrame has loaded
        try:
            WebDriverWait(driver, 5).until(
                ExpCond.presence_of_element_located((By.ID, "duo_iframe"))
            )
        except:
            status_text = driver.find_element_by_id("status").text
            if status_text == "Invalid credentials.":
                print("Your credentials were invalid. Please try again!")
            elif status_text != "":
                print("The following authentication error occurred: " + status_text)
            else:
                print("Login timed out. Please check your internet connection.")
            return False

        # Switch to the Duo Security iFrame
        driver.switch_to.frame(0)

        btn_2fa_xpath = "html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button"

        # Wait until the button has been loaded
        WebDriverWait(driver, 5).until(
            ExpCond.element_to_be_clickable((By.XPATH, btn_2fa_xpath)))

        driver.find_element(By.XPATH, btn_2fa_xpath).click()

        print("Please check your push notifications and accept it within 25 seconds.")

        # Switch back to the original page
        driver.switch_to.default_content()

        WebDriverWait(driver, 25).until(
            ExpCond.url_changes(URL_AUTH_PORTAL)   
        )

        return True

    except Exception as e:
        print("Something bad happened here. We got this error:", e)
        print("Here's the traceback (for advanced users):")
        
        import traceback  
        traceback.print_exc()

        driver.quit()

    return False
