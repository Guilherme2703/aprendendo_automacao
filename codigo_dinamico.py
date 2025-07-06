from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        servico = Service(executable_path=r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service=servico, options=chrome_options)
        self.site = input('A qual site gostaria de ir: ')
    
    def Iniciar(self):
        self.driver.get(self.site)
        time.sleep(100)
        
curso =  CursoAutomacao()
curso.Iniciar()