from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def processamento():
    print("✅ Concluído com sucesso!")

def filter_search(empresa, cidade):
    
    # Configurações para abrir um perfil do Chrome Driver ja logado no linkedin
    options = Options()
    options.add_argument("--user-data-dir=C:\\Users\\Study\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("--profile-directory=Default")  # ou "Profile 1"
    options.add_argument("--disable-blink-features=AutomationControlled")  # menos chance de detecção
    driver = webdriver.Chrome(options=options)

    # Tempo máximo de espera
    wait = WebDriverWait(driver, 15)
    # Coordenadas da tela para seleção de empresa - Tentiva por métodos convencionais não funcionaram (xpath, id, etc)
    cordsx = 934 
    cordsy = 191

    # Abre o Site com a palvra chave dentro do link de pesquisa
    driver.get(f"https://www.linkedin.com/search/results/all/?keywords={empresa}&origin=GLOBAL_SEARCH_HEADER&sid=z.y")  # já logado se o perfil estiver certo!
    time.sleep(5)

    # Espera o botão "Pessoas" e clica
    botao_pessoas = wait.until(EC.element_to_be_clickable((
        By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div[1]/div/div/div/section/ul/li[3]/button')))
    botao_pessoas.click()
    # Ver todos os resultados de pessoas
    ver_todos = wait.until(EC.element_to_be_clickable((
        By.PARTIAL_LINK_TEXT, "Ver todos os resultados de pessoas")))
    ver_todos.click()

    # Filtro localidade
    filtro_local = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchFilter_geoUrn")))
    filtro_local.click()
    # Colocar cidade
    driver.find_element(By.CSS_SELECTOR, 'input.basic-input[aria-label="Adicionar localidade"]').click()
    driver.find_element(By.CSS_SELECTOR, f'input.basic-input[aria-label="Adicionar localidade"]').send_keys({cidade})
    time.sleep(1)
    # Aguarda aparecer a sugestão no popup
    sugestao = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.basic-typeahead__selectable[role="option"]')))
    sugestao.click()
    driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[2]/section/div/nav/div/ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]').click()

    # Filtro Empresa Atual
    filtro_empresa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchFilter_currentCompany")))
    filtro_empresa.click()
    # Move o cursor para a coordenada e clica
    actions = ActionChains(driver)
    actions.move_by_offset(cordsx, cordsy).click().perform()
    actions.move_by_offset(-cordsx, -cordsy).perform()
    resultados = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[3]/div[2]/section/div/nav/div/ul/li[6]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span')))
    resultados.click()
    time.sleep(2) # fechar


    return processamento()