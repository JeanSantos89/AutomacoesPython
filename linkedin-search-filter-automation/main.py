from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from exec import filter_search
import time

# Solicita a palavra chave de pesquisa, por exemplo: Sicredi, amazon, etc
empresa = input("Qual empresa deseja filtrar? " )
cidade = input("Qual cidade deseja filtrar?\n Exemplo: Cidade, Estado\n")
filter_search(empresa, cidade)