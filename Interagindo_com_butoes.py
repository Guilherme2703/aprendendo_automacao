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
        
        # Entrando na pagina de login
        try:
            botao = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//a[@href="https://zcursos.me/index.php?route=account/download"]')
                    )
                )
            botao.click()
        except TimeoutException:
            print("Botão não encontrado")
        
        time.sleep(5)
        # Preenchendo o campo de E-mail
        
        try:
            campo_email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@id="input-email"]')
                    )
                )
            campo_email.click()
            campo_email.send_keys('email usand o no cadastro')

        except TimeoutException:
            pass
        
        time.sleep(2)
        
        # Preenchendo o campo senha
        try:
            campo_senha = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@id="input-password"]')
                    )
                )
            campo_senha.click()
            campo_senha.send_keys('A senha que vc usou no cadastro')

        except TimeoutException:
            pass
        
        try:
            acessar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@type="submit"]')
                    )
                )
            acessar.click()
        except TimeoutException:
            print("Botão não encontrado")
        
        input("Precione qualquer botão para finalizar a automaçao")

        
curso =  CursoAutomacao()
curso.Iniciar()

