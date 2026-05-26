from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://127.0.0.1:5500/login.html")

driver.maximize_window()

time.sleep(2)

driver.find_element(By.ID, "correo").send_keys("linaportela2002@gmail.com")

driver.find_element(By.ID, "contrasena").send_keys("incorrecta")

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

# CAPTURAR ALERTA
alerta = driver.switch_to.alert

print("Mensaje alerta:", alerta.text)

alerta.accept()

time.sleep(2)

driver.save_screenshot("login_fallido.png")

driver.quit()