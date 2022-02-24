from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait         
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By                   
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import numpy as np
import opciones 


# Iniciar sesión
def login():
    opciones.driver.get('https://www.instagram.com/accounts/login/')
    username = input('Ingrese su nombre de usuario: ')
    password = input('Ingrese su contraseña: ')

    opciones.wait.until(
        EC.presence_of_element_located((
            By.NAME,
            'username'
        ))
    ).send_keys(username)

    time.sleep(np.random.uniform(3.0, 5.0))

    opciones.wait.until(
        EC.presence_of_element_located((
            By.NAME,
            'password'
        ))
    ).send_keys(password, Keys.ENTER)

    # 2FA code - Descomentar en caso de usar
    code = input("Insertar código 2FA (ingrese 0 en caso de no utilizar 2FA): ")
    if code != "0":
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_2hvTZ.pexuQ.zyHYP'))).send_keys(code_2FA, Keys.ENTER)
        opciones.driver.find_element(By.NAME, 'verificationCode').send_keys(code)
        
        time.sleep(np.random.uniform(4.0, 8.0))
        
        opciones.driver.find_element(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF').click()
        print("Verificando...")
    
    return username
