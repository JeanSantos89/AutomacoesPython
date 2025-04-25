from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument(r"C:\Users\Study\AppData\Local\Google\Chrome\User Data\Default")
options.add_argument("--profile-directory=Default")
browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome() # Abrir navegador
browser.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AXH0vVvGfVZJvZtyzBH1Ucoo2GgdCq_mA1QcGKNzQF7qfG2vUssGzY-nTK0ffcoHV_EAuhSQYNzyjQ&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1575003196%3A1744056841861385")
browser.maximize_window() 

login = "#"
senha = "#"


## LOGIN
browser.find_element("id", "identifierId").click()
browser.find_element("id", "identifierId").send_keys(login)
browser.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
WebDriverWait(browser, 9999).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span')) # Expected espera receber uma tupla, por isso, dois parênteses
)


browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').click()
browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(senha)
browser.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()

time.sleep(10)



