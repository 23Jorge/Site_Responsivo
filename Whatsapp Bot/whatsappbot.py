#Importar as bibliotecas
#Navegar até o Whatsapp web
#Buscar contatos e grupos
#Enviar mensagens para contatos e grupos

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
#Navegar até whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
time.sleep(30)
#definir contatos e grupos e mensagens a ser enviada
contatos = ['Meus Estudos', 'Amor']