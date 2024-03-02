import webbrowser 
import os

def open_google():
    url = 'http://google.com'
    webbrowser.open_new_tab(url)

def open_notepad():
    os.system("notepad.exe")

def open_terminal(): 
    os.system("start cmd.exe")

def open_settings(): 
    os.popen("start ms-settings:")

if __name__ == "__main__":
    open_settings()