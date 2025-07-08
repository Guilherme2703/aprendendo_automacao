import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        servico = Service(executable_path=r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service=servico, options=chrome_options)
    
    def Iniciar(self):
        self.driver.get('https://zcursos.me/')
        
        try:
            botao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//a[@class="dropdown-toggle"]')
                    )
                )
            print("Botão encontrado")

            botao.click()
            
        except TimeoutException:
            print("Botão não encontrado")
        
        
        input("Precione qualquer botão para finalizar a automaçao")

        
curso =  CursoAutomacao()
curso.Iniciar()

