import webbrowser 
import os

# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# opens a google browser
def open_google(): 
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://google.com")

    return driver 

# types given text in search bar
def search_google(driver, text):
    driver.switch_to.window(driver.window_handles[0])
    search_input = driver.find_element("name", "q")

    search_input.send_keys(text)
    time.sleep(2)
    search_input.submit()


def open_notepad():
    os.system("notepad.exe")

def open_terminal(): 
    os.system("start cmd.exe")

def open_settings(): 
    os.popen("start ms-settings:")

if __name__ == "__main__":
    driver = open_google()
    search_google(driver, "what's good")