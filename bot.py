# import pyautogui as pg
# import os, time, subprocess
from pymsgbox import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


#Initialize global variables
domain_names = prompt(text='Comma Seperated Domains', title='Calander Bot').lower().replace(" ", "").split(",")


def LK_domain(url, prefix):
    # Set up ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode

    # Create Chrome driver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    # Open the webpage
    driver.get('https://www.domains.lk/' )

    # Find the input field and send keys
    input_field = driver.find_element(By.ID, 'mod_domain-search-searchword')  # Replace 'input-id' with the actual ID of the input field
    input_field.send_keys(url)

    # Simulate hitting Enter
    input_field.send_keys(Keys.RETURN)

    # # Wait for a specific element to load on the page
    wait = WebDriverWait(driver, 10)  # Adjust the timeout (in seconds) as needed
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'domainsearchpage-registered-info')))  # Replace 'element-id' with the ID of the element you want to wait for

    element = driver.find_element(By.CSS_SELECTOR, '.row.domainsearchpage-registered-row .col-sm-6 .domainsearchpage-registered-info.ng-binding')  # Replace 'h1' with the appropriate CSS selector for the element
    date = element.text
    print(f"{prefix} {url} renewal due {date}")

def INT_domain(url, prefix):
    # Set up ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode

    # Create Chrome driver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    # Open the webpage
    driver.get("https://www.whatsmydns.net/domain-expiration?q=" + url)

    # # Wait for a specific element to load on the page
    wait = WebDriverWait(driver, 10)  # Adjust the timeout (in seconds) as needed
    element = wait.until(EC.presence_of_element_located((By.ID, 'date'))) 

    element = driver.find_element(By.ID, 'date')
    date = element.text
    print(f"{prefix} {url} renewal due {date}")
    


#Loop over domains and perform operations
for url in domain_names:
    url_parts = url.split(".")
    if(url_parts[1] == "lk"):
        LK_domain(url, "DOMAIN")
    else:
        INT_domain(url, "DOMAIN")