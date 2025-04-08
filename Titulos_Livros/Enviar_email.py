from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

def lancar_email(destinatario, tipo_livro, titulos_livros):
    options = Options()
    options.add_argument("--user-data-dir=C:\\Users\\Study\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("--profile-directory=Profile 1")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(3)

    # Clica no botão "Escrever"
    driver.find_element(By.XPATH, "//div[text()='Escrever']").click()
    #time.sleep(3)

    # Preenche os campos do e-mail
    driver.switch_to.active_element.send_keys(destinatario)
    driver.find_element(By.NAME, "subjectbox").send_keys(f"Títulos dos livros - Categoria: {tipo_livro}")

    corpo_email = "\n".join(titulos_livros)
    driver.find_element(By.XPATH, "//div[@aria-label='Corpo da mensagem']").send_keys(corpo_email)

    # Clica em "Enviar"
    driver.find_element(By.XPATH, "//div[text()='Enviar']").click()
    time.sleep(10)
    driver.quit()
