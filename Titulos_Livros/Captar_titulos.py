from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Enviar_email import lancar_email  # sem acento

TipoLivro = "Mystery"
TitulosLivros = []

driver = webdriver.Chrome()
driver.get("http://books.toscrape.com/")
driver.maximize_window()

busca = driver.find_element(By.XPATH, f"//a[contains(text(), '{TipoLivro}')]")
busca.click()
time.sleep(3)

while True:
    livros = driver.find_elements(By.CLASS_NAME, "product_pod")
    for livro in livros:
        titulo = livro.find_element(By.TAG_NAME, "h3").text
        TitulosLivros.append(titulo)
        print(titulo)
    try:
        driver.find_element(By.XPATH, '//*[@id="default"]/div/div/div/div/section/div[2]/div/ul/li[2]/a').click()
        time.sleep(3)
    except:
        break

driver.quit()

destinatario = input("Para quem deseja enviar esse email? ")
lancar_email(destinatario, TipoLivro, TitulosLivros)
