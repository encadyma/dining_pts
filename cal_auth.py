## A script to authenticate the current user
## with CalNet, given a Selenium Webdriver
## instance.

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCond
from selenium.webdriver.common.by import By

def auth_calnet(driver, username, password):
    try:
        driver.get(URL_AUTH_PORTAL)
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
                print("Login timed out. Please check your internet connection Please check your internet connection.")
            return False

        # Switch to the Duo Security iFrame
        driver.switch_to.frame(0)

        btn_2fa_xpath = "html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button"

        # Wait until the button has been loaded
        WebDriverWait(driver, 5).until(
            ExpCond.element_to_be_clickable((By.XPATH, btn_2fa_xpath)))

        driver.find_element(By.XPATH, btn_2fa_xpath).click()

        print("Please check your push notifications and accept it within 15 seconds.")

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

# THIS IS TEST CODE
# PLEASE DELETE AND MOVE TO CLI!

import os
from constants import *
from selenium import webdriver

from selenium.webdriver.firefox.options import Options

driver_options = Options()
driver_options.headless = True

print(" ~~~~~ CAL DINING CHECKER ~~~~~ ")
print(" >  mini script by @encadyma  < ")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")



print("""\n
>> NOTICE!
   This program is still in development.
   Unintended behavior may result from the use of this program.
   Further usage of this program means that you run this program at your own risk.

   IMPORTANT: DO NOT TRUST YOUR PASSWORDS IN THE WRONG HANDS!
   Always double check the source code of what you are running.
   You may safely quit this application through CTRL+C.\n
""")

from getpass import getpass

print("Please authenticate into your account!")
cal_uid = raw_input("Enter your CalNet username: ")
cal_pass = getpass("Enter your password (this is hidden): ")

driver = webdriver.Firefox(
        executable_path=os.path.abspath("geckodriver"),
        options=driver_options)
print("We're authenticating you in as soon as possible...")

if auth_calnet(driver, cal_uid, cal_pass):
    print("Loading balances from Cal Dining and Housing...")
    driver.get(URL_BALANCES_PORTAL)

    btn_view_bal = "html/body/div/div[3]/div/div/div/div[1]/div/div[3]/a"

    WebDriverWait(driver, 3).until(
        ExpCond.element_to_be_clickable((By.XPATH, btn_view_bal))
    )

    driver.find_element(By.XPATH, btn_view_bal).click()
    
    # This is specific to a certain configuration.
    txt_sid = "/html/body/div/div[3]/div/div/div/div[2]/div/table/tbody/tr[3]/td/b"
    txt_flex = "/html/body/div/div[3]/div/div/div/div[2]/div/table/tbody/tr[7]/td[1]/b"

    def get_txt(xpath):
        elem = driver.find_element(By.XPATH, xpath)
        return elem.text

    print("============ STUDENT INFO ============")
    print("Your student ID is " + get_txt(txt_sid))
    print("Your remaining flex dollars: " + get_txt(txt_flex))
    driver.quit()

else:
    print("Quitting this application...")
    driver.quit()
