from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abrir registro
driver.get("http://127.0.0.1:5500/registro.html")

driver.maximize_window()

time.sleep(2)

# Nombre
driver.find_element(By.ID, "nombreApellido").send_keys("Prueba Selenium")

# Correos diferentes
driver.find_element(By.ID, "correo").send_keys("correo1@test.com")

driver.find_element(By.ID, "confirmarCorreo").send_keys("correo2@test.com")

# Teléfono
driver.find_element(By.ID, "telefono").send_keys("3001234567")

# Contraseña
driver.find_element(By.ID, "contrasena").send_keys("12345678")

driver.find_element(By.ID, "confirmarContrasena").send_keys("12345678")

# Checkbox
driver.find_element(By.ID, "notrobot").click()

time.sleep(1)

# Click botón
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

# Capturar alerta
alerta = driver.switch_to.alert

print("Mensaje alerta:", alerta.text)

# Screenshot evidencia
driver.save_screenshot("CP-004.png")

# Aceptar alerta
alerta.accept()

time.sleep(2)

driver.quit()