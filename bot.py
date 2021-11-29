import pyautogui
import webbrowser as wb
import time
import urllib3
import beautiful

#teste
#import mecanizar
#import scrapemark
#import scrapy


wb.open("https://web.whatsapp.com")
for j in range(30):
    time.sleep(1)
    print(j)

for i in range(10):
    pyautogui.press("o")
    pyautogui.press("enter")

