# Como obter porxies
# Como usar porxies
# Cuidados
# 51.81.245.3	1798

import time 
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


PROXY = '200.174.198.86:8888'

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={PROXY}')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_webdriver = os.getcwd() + os.sep + 'chromedriver.exe'
servico = Service(executable_path=chrome_webdriver)

driver =  webdriver.Chrome(service=servico, options=chrome_options)

driver.get('https://whatismyip.com.br/')
input('Precione enter para finalizar o programa')