import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox("/home/user/.mozilla/firefox/chgnbc65.default-release",executable_path="./drivers/geckodriver")


browser.get('https://dashboard.twitch.tv/u/vigia_123/stream-manager')

for i in range(10):
    time.sleep(1)
    print(i)

size = 0

for i in range(100000):
    size = size+1
    time.sleep(1)
    elements = browser.find_elements_by_class_name('text-fragment')
    i = len(elements)
    print('Qt :%d' %i)
    if i > 0:
        print(elements[i-1].text)
    else:
        print('Texto: Sem texto...')
    if size > 20:
        size = 0
        parei aqui...
        button = browser.find_element('ScCoreButton-sc-1qn4ixc-0 ScCoreButtonPrimary-sc-1qn4ixc-1 jGqsfG ksFrFH')

        # clicking on the button
        button.click()


