import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox("/home/user/.mozilla/firefox/chgnbc65.default-release",executable_path="./drivers/geckodriver")


browser.get('https://dashboard.twitch.tv/u/vigia_123/stream-manager')

for i in range(10):
    time.sleep(1)
    print(i)

size = 0

for i in range(100000):
    size = size+1
    time.sleep(0.01)
    elements = browser.find_elements(By.CLASS_NAME,"text-fragment")
    i = len(elements)
    #print('Qt :%d' %i)
    if i > 0:
        print(elements[i-1].text)
    else:
        print('Texto: Sem texto...')
    if size > 200:
        size = 0
        text_area = browser.find_element(By.CSS_SELECTOR,".ScInputBase-sc-1wz0osy-0")
        text_area.send_keys("/clear")
        button = browser.find_element(By.CSS_SELECTOR,".faqhMI > div:nth-child(1)")
        button.click()
        #.evtFDZ
        #.eZactg
        #.eZactg
        


