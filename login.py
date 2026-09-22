import os #Manipula caminhos de arquivos, diretorios e recursos do sistema operacional
import time #Módulo para manipulação de tempo
from selenium import webdriver #Módulo para controlar os navegadores
from selenium.webdriver.chrome.options import Options #Classe responsável por definir parametro e preferencias de incialização
from selenium.webdriver.chrome.service import Service #Executa e administra o Chrome Driver Manager
from webdriver_manager.chrome import ChromeDriverManager #Responsável por verificar e atualizar a versão do Chrome Drive Manager de acordo com a versão do chrome

#Criei uma variavel que tem o caminho absoluto do meu chrome_profile
chrome_profile = os.path.join(os.getcwd(), "chrome_profile")

#Configurandoa o perfil de incialização
settings = Options()
settings.add_argument(f'--user-data-dir={chrome_profile}')


#Na variavel service estou informando onde está o meu chrome Drive Manager
service = Service(ChromeDriverManager().install())
# Estou dizendo onde é para buscar o Chrome Drive Manager e o perfil
navegador = webdriver.Chrome(service = service, options = settings)

#Executar o login
try:
    navegador.get("https://portal.office.com")
    input("Aperte Enter após concluir o login....")
finally:
    navegador.quit()