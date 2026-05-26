from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://127.0.0.1:5500/registro.html")

driver.maximize_window()

time.sleep(2)

# LLENAR FORMULARIO
driver.find_element(By.ID, "nombreApellido").send_keys("Usuario Selenium")

driver.find_element(By.ID, "correo").send_keys("selenium1@test.com")

driver.find_element(By.ID, "confirmarCorreo").send_keys("selenium1@test.com")

driver.find_element(By.ID, "telefono").send_keys("3001234567")

driver.find_element(By.ID, "contrasena").send_keys("Ensayando")

driver.find_element(By.ID, "confirmarContrasena").send_keys("Ensayando")

driver.find_element(By.ID, "notrobot").click()

time.sleep(1)

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(3)

if "login.html" in driver.current_url:
    print("✅ Registro exitoso")
else:
    print("❌ Registro falló")

driver.save_screenshot("registro_exitoso.png")

time.sleep(2)

driver.quit()