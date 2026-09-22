import os #Manipula caminhos de arquivos, diretorios e recursos do sistema operacional
import time #Módulo para manipulação de tempo
from selenium import webdriver #Módulo para controlar os navegadores
from selenium.webdriver.chrome.options import Options #Classe responsável por definir parametro e preferencias de incialização
from selenium.webdriver.chrome.service import Service #Executa e administra o Chrome Driver Manager
from webdriver_manager.chrome import ChromeDriverManager #Responsável por verificar e atualizar a versão do Chrome Drive Manager de acordo com a versão do chrome


#URLS de acesso:
urls_planilhas = {
    "fibra": "**" ,
    "eventos": "**" ,
    "ferramentas": "**"
}

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
    navegador.get(urls_planilhas["fibra"])
    input("Aperte Enter após concluir o login....")
    navegador.switch_to.new_window('tab')
    navegador.get(urls_planilhas["eventos"])
    navegador.switch_to.new_window('tab')
    navegador.get(urls_planilhas["ferramentas"])
    input("Aperte Enter após concluir a abertura....")
finally:
    navegador.quit()