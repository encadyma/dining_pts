## The CLI interface for the Dining
## Pts application.

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCond
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from constants import *
from cal_auth import auth_calnet

print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 CAL DINING CHECKER                 
              mini script by @encadyma
                   (revision 001)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

print("""
>> NOTICE!
   This program is still in development.
   Unintended behavior may result from the use of this program.
   Further usage of this program means that you run this program at your own risk.

   IMPORTANT: DO NOT TRUST YOUR PERSONAL DATA IN THE WRONG HANDS!
   Always double check the source code of what you are running.
   You may safely quit this application through CTRL+C.
""")

driver_options = Options()
# driver_options.headless = True

driver = webdriver.Firefox(
    executable_path=os.path.abspath("geckodriver"),
    options=driver_options)

if auth_calnet(driver):
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

    if len(driver.find_elements(By.XPATH, txt_flex)) > 0:
        print("Your remaining flex dollars: " + get_txt(txt_flex))
    else:
        print("Unfortunately, you are not on a meal plan.")
    
    driver.quit()

else:
    print("Authentication failed. Quitting this application...")
    driver.quit()
