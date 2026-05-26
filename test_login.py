from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://127.0.0.1:5500/login.html")

# MAXIMIZAR VENTANA
driver.maximize_window()

time.sleep(2)

driver.find_element(By.ID, "correo").send_keys("linaportela2002@gmail.com")

driver.find_element(By.ID, "contrasena").send_keys("123456")

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(3)

# VERIFICAR SI ENTRÓ AL DASHBOARD
if "dashboard.html" in driver.current_url:
    print("✅ Login exitoso")
else:
    print("❌ Login falló")

time.sleep(2)

driver.save_screenshot("login_exitoso.png")

# CERRAR NAVEGADOR
driver.quit()