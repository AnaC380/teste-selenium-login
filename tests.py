from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Iniciar o navegador
driver = webdriver.Chrome()

# Acessar a página de login
driver.get("https://practicetestautomation.com/practice-test-login/")

# Esperar a página carregar (só para garantir)
time.sleep(2)

# Preencher o campo de usuário
driver.find_element(By.ID, "username").send_keys("student")

# Preencher o campo de senha
driver.find_element(By.ID, "password").send_keys("Password123")

# Clicar no botão de login
driver.find_element(By.ID, "submit").click()

# Esperar o resultado
time.sleep(2)

# Verificar se o login foi bem-sucedido
if "Logged In Successfully" in driver.page_source:
    print("✅ Teste passou!")
else:
    print("❌ Teste falhou.")

# Fechar o navegador
driver.quit()
