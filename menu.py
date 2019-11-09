from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCond
from selenium.webdriver.common.by import By

from six.moves import input as raw_input

from constants import *

def menu_loop(driver):
    print("""
    MENU Options
    (S) Retrieve usage statistics for meal swipes.
    (F) Retrieve usage statistics for flex dollars.
    (Q) Quit this application
    """)

    next_choice = raw_input("Please enter in your choice: ").upper()
    
    print("")

    if next_choice == "Q":
        if raw_input("Are you sure you want to quit the application (Y/N)? ").lower() == 'y':
            import sys
            sys.exit()
    elif next_choice == "F":
        # TODO: Move this code to a function
        # that extracts table data.
        print("RETRIEVING the usage statistics for flex dollars...\n")
        driver.get(URL_BALANCES_FLEX)

        flex_table_xpath = "html/body/div/div[3]/div/div/div/div[2]/div/table/tbody"

        WebDriverWait(driver, 5).until(
            ExpCond.presence_of_element_located((By.XPATH, flex_table_xpath))
        )

        rows = driver.find_elements(By.XPATH, flex_table_xpath + '/tr')
        print("There are a total of {} entries found.".format(len(rows) - 2))

        if len(rows) > 2:
            print("Your latest charge was " + rows[2].text)

    elif next_choice == "S":
        print("RETRIEVING the usage statistics for meal swipes...\n")
        driver.get(URL_BALANCES_MP)

        flex_table_xpath = "html/body/div/div[3]/div/div/div/div[2]/div/table/tbody"

        WebDriverWait(driver, 5).until(
            ExpCond.presence_of_element_located((By.XPATH, flex_table_xpath))
        )

        rows = driver.find_elements(By.XPATH, flex_table_xpath + '/tr')
        print("There are a total of {} entries found.".format(len(rows) - 2))

        if len(rows) > 2:
            print("Your latest swipe was " + rows[2].text)

    else:
        print("Choice not recognized. Please use the menu options to navigate.")

    print("")

    menu_loop(driver)