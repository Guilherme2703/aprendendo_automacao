from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--window-size=800,800')
        servico = Service(executable_path=r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service=servico, options=chrome_options)
    
    def Iniciar(self):
        self.driver.get('https://www.instagram.com') 
        self.driver.maximize_window() 
        self.driver.refresh() 
        self.driver.get()  
        self.driver.back()
        self.driver.forward()



curso =  CursoAutomacao()
curso.Iniciar()


# | Método                                   | Descrição                                                   |
# | ---------------------------------------- | ----------------------------------------------------------- |
# | `get(url)`                               | Abre a URL especificada no navegador.                       |
# | `close()`                                | Fecha a aba atual do navegador.                             |
# | `quit()`                                 | Encerra o navegador inteiro (todas as janelas).             |
# | `find_element(by, value)`                | Encontra um único elemento no DOM.                          |
# | `find_elements(by, value)`               | Encontra todos os elementos que correspondem ao critério.   |
# | `execute_script(script, *args)`          | Executa JavaScript no contexto da página atual.             |
# | `execute_async_script(script, *args)`    | Executa JavaScript assíncrono.                              |
# | `get_screenshot_as_file(filename)`       | Tira uma screenshot da tela e salva como arquivo.           |
# | `get_screenshot_as_png()`                | Tira uma screenshot e retorna em bytes (PNG).               |
# | `get_window_size()`                      | Retorna o tamanho da janela atual.                          |
# | `set_window_size(width, height)`         | Define o tamanho da janela do navegador.                    |
# | `maximize_window()`                      | Maximiza a janela do navegador.                             |
# | `minimize_window()`                      | Minimiza a janela do navegador.                             |
# | `fullscreen_window()`                    | Coloca a janela em modo tela cheia.                         |
# | `get_window_handle()`                    | Retorna o identificador da janela atual.                    |
# | `window_handles`                         | Lista de identificadores de todas as janelas abertas.       |
# | `switch_to.window(handle)`               | Troca o controle para outra aba/janela.                     |
# | `switch_to.frame(frame_reference)`       | Muda o foco para um `iframe` específico.                    |
# | `switch_to.default_content()`            | Volta o foco para o conteúdo principal (fora de `iframe`).  |
# | `switch_to.alert`                        | Acessa um alerta ativo (JavaScript alert, confirm, prompt). |
# | `back()`                                 | Volta uma página no histórico do navegador.                 |
# | `forward()`                              | Avança uma página no histórico.                             |
# | `refresh()`                              | Recarrega a página atual.                                   |
# | `current_url`                            | Retorna a URL atual.                                        |
# | `title`                                  | Retorna o título da página.                                 |
# | `page_source`                            | Retorna o código-fonte HTML da página.                      |
# | `current_window_handle`                  | Identificador da janela atual.                              |
# | `implicitly_wait(time_in_seconds)`       | Define um tempo de espera implícito.                        |
# | `set_page_load_timeout(time_in_seconds)` | Define tempo máximo para carregamento da página.            |
# | `set_script_timeout(time_in_seconds)`    | Define tempo máximo para scripts JS assíncronos.            |
