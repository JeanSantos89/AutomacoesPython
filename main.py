from selenium import webdriver  # Importa biblioteca webDriver
import time  # Importa biblioteca time
from selenium.webdriver.common.by import By  # Importa a classe By para localizar elementos
from selenium.webdriver.support.ui import WebDriverWait  # Para espera 
from selenium.webdriver.support import expected_conditions as EC  # Para condições de espera

# Solicita o primeiro nome até que o usuário forneça uma resposta válida
PrimeiroNome = input("Qual seu primeiro nome? ")
while not PrimeiroNome: # Se o campo estiver vazio, repete a solicitação
    PrimeiroNome = input("Por favor, forneça seu primeiro nome: ")

# Solicita o sobrenome até que o usuário forneça uma resposta válida
Sobrenome = input("Qual seu sobrenome? ")
while not Sobrenome:  # Se o campo estiver vazio, repete a solicitação
    Sobrenome = input("Por favor, forneça seu sobrenome: ")

# Inicia o navegador
navegador = webdriver.Chrome()  
navegador.get("https://docs.google.com/forms/d/1gTVHqXM-X2QGLNw_OMJj6wdn_588QK9zWjkZ6kCN1Xk/edit")  
navegador.maximize_window()  # Abre em tela cheia

WebDriverWait(navegador, 10).until( # Tela fica em espera até que o campo Primeiro Nome esteja disponivel para inserção
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
)

# Localiza os campos para o primeiro nome e sobrenome por XPATH
PrimeiroNomeInput = navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
PrimeiroNomeInput.send_keys(PrimeiroNome)

SobrenomeInput = navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
SobrenomeInput.send_keys(Sobrenome)

WebDriverWait(navegador, 2).until( # Tela fica em espera até que o botão de inserir informações esteja clicavel
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))
)

# Localiza e clica no botão de envio 
botao = navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
botao.click()

