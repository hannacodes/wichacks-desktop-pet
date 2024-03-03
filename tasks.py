import os
# pip install selenium
from selenium import webdriver

# opens a google browser
def open_google(): 
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(200, 300)
    driver.set_window_size(1000, 520)
    driver.get("http://google.com")

    return driver 

# types given text in search bar
def search_google(driver):
    driver.switch_to.window(driver.window_handles[0])
    search_input = driver.find_element("name", "q")

    #search_input.send_keys(text)
    search_input.submit()

def open_notepad():
    os.system("notepad.exe")

def open_terminal(): 
    os.system("start cmd.exe")

def open_settings(): 
    os.popen("start ms-settings:")
