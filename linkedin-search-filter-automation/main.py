from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Solicita a palavra chave de pesquisa, por exemplo: Sicredi, amazon, etc
PalavraChave = input("Qual a palvra chave? Empresa, nome de pessoa, instituição... " )

# Configurações para abrir um perfil do Chrome Driver ja logado no linkedin
options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Study\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Default")  # ou "Profile 1"
#options.add_argument("--headless=new")  # modo invisível (pode remover pra testar)
options.add_argument("--disable-blink-features=AutomationControlled")  # menos chance de detecção
driver = webdriver.Chrome(options=options)


# Abre o Site com a palvra chave dentro do link de pesquisa
driver.get(f"https://www.linkedin.com/search/results/all/?keywords={PalavraChave}&origin=GLOBAL_SEARCH_HEADER&sid=z.y")  # já logado se o perfil estiver certo!
time.sleep(3)

# Clica no botão pessoas
driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div[1]/div/div/div/section/ul/li[3]/button').click()
time.sleep(2)

# Ver todos os resultados
driver.find_element(By.PARTIAL_LINK_TEXT, "Ver todos os resultados de pessoas").click()
time.sleep(2)

# Filtro localidade
driver.find_element(By.CSS_SELECTOR, "#searchFilter_geoUrn").click()
time.sleep(2)

# Colocar cidade
driver.find_element(By.CSS_SELECTOR, 'input.basic-input[aria-label="Adicionar localidade"]').click()
driver.find_element(By.CSS_SELECTOR, 'input.basic-input[aria-label="Adicionar localidade"]').send_keys("Ponta Grossa, Paraná")
time.sleep(2)
# Aguarda aparecer a sugestão no popup
sugestao = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.basic-typeahead__selectable[role="option"]'))
)
sugestao.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button#ember304').click()
time.sleep(2)


#driver.find_element(By.CSS_SELECTOR, '.basic-typehead__triggered-content ').click()
#elemento = driver.find_element(By.CSS_SELECTOR, 'div.basic-typehead__triggered_content[role="listbox"]')
#elemento.click()
#time.sleep(7)



#driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[5]/div/div[2]/a').click()
#time.sleep(10)
#botao = driver.find_element(By.XPATH, "//button[contains(text(), 'Ver todos os resultados de pessoas')]")
#botao.click()



# Clica em localidade
#time.sleep(16)
#driver.find_element(By.XPATH, '//*[@id="searchFilter_geoUrn"]').click()
#botao = driver.find_element(By.XPATH, "//button[contains(text(), 'Ver todos os resultados de pessoas')]")
#botao.click()




#driver.find_element(By.XPATH, '//*[@id="artdeco-hoverable-artdeco-gen-83"]/div[1]/div/form/fieldset/div[1]/div/div/input').send_keys("Ponta Grossa, Paraná, Brasil")
#WebDriverWait(driver, 2).until(
#    EC.element_to_be_clickable((By.XPATH, '//*[@id="artdeco-hoverable-artdeco-gen-83"]/div[1]/div/form/fieldset/div[1]/ul/li[1]/label/p')) # Expected espera receber uma tupla, por isso, dois parênteses
#)
#driver.find_element(By.XPATH, '//*[@id="artdeco-hoverable-artdeco-gen-83"]/div[1]/div/form/fieldset/div[1]/ul/li[1]/label/p').click()
#WebDriverWait(driver, 2).until(
#    EC.element_to_be_clickable((By.XPATH, '//*[@id="ember495"]/span')) # Expected espera receber uma tupla, por isso, dois parênteses
##)
#driver.find_element(By.XPATH, '//*[@id="ember495"]/span').click()
#time.sleep(3)


