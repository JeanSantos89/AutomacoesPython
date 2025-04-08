from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from setup_email import enviar_email  # certifique-se que setup_email.py está na mesma pasta

generos = [
    "Travel", "Mystery", "Historical Fiction", "Sequential Art", "Classics", "Philosophy",
    "Romance", "Womens Fiction", "Fiction", "Childrens", "Religion", "Nonfiction",
    "Music", "Default", "Science Fiction", "Sports and Games", "Add a comment", "Fantasy",
    "New Adult", "Young Adult", "Science", "Poetry", "Paranormal", "Art", "Psychology",
    "Autobiography", "Parenting", "Adult Fiction", "Humor", "Horror", "History",
    "Food and Drink", "Christian Fiction", "Business", "Biography", "Thriller",
    "Contemporary", "Spirituality", "Academic", "Self Help", "Historical", "Christian",
    "Suspense", "Short Stories", "Novels", "Health", "Politics", "Cultural", "Erotica", "Crime"
]

print("\nGÊNEROS DISPONÍVEIS:\n" + "-" * 60)
for i in range(0, len(generos), 3):
    print("".join(f"{g:<25}" for g in generos[i:i+3]))
print("-" * 60)

TipoLivro = input("Qual gênero de livro deseja ver os títulos? ")
TitulosLivros = []

driver = webdriver.Chrome()
driver.get("http://books.toscrape.com/")
driver.maximize_window()

# Clica na categoria desejada
busca = driver.find_element(By.XPATH, f"//a[contains(text(), '{TipoLivro}')]")
busca.click()
time.sleep(3)

# Captura os títulos de todas as páginas
while True:
    livros = driver.find_elements(By.CLASS_NAME, "product_pod")
    for livro in livros:
        titulo = livro.find_element(By.TAG_NAME, "h3").text
        TitulosLivros.append(titulo)
        print(titulo)
    try:
        proxima_pagina = driver.find_element(By.XPATH, '//li[@class="next"]/a')
        proxima_pagina.click()
        time.sleep(3)
    except:
        break

driver.quit()

# Enviar email
destinatario = input("Para quem deseja enviar esse email? ")
enviar_email(destinatario, TipoLivro, TitulosLivros)
