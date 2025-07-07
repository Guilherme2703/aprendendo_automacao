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
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//a[@class="dropdown-toggle"]')
                    )
                )
            print("Botão encontrado")
        except TimeoutException:
            print("Botão não encontrado")

        
curso =  CursoAutomacao()
curso.Iniciar()

# | O que você quer selecionar            | XPath                                 |
# | ------------------------------------- | ------------------------------------- |
# | Elemento por ID                       | `//*[@id="meuId"]`                    |
# | Elemento por texto exato              | `//button[text()="Enviar"]`           |
# | Elemento por texto que contém         | `//a[contains(text(),"Clique aqui")]` |
# | Elemento por atributo                 | `//input[@type="email"]`              |
# | Primeiro item de uma lista            | `(//ul/li)[1]`                        |
# | Um botão dentro de um form específico | `//form[@id="loginForm"]//button`     |
