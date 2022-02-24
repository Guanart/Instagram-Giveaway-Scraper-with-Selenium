from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait         
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By                     
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup
import time
import numpy as np
import os
import shutil
# Mis módulos
import opciones
import login

# Login
print("Loggeando...")
username = login.login()

# URL del sorteo
sorteo = input("Ingrese la URL del sorteo: ")
print("Cargando sorteo...")
opciones.driver.get(sorteo)

### Scraping de todos los usuarios
# Cargar los comentarios haciendo click en el botón
clicks = int(input("Número de click al botón +comentarios: "))
print('Scrapeando usuarios...')

try:
    for i in range(clicks):                                                                 # 20 clicks al botón
        try:                                                                            # Usamos cláusulas try...for para evitar que se pare el script ante cualquier error
            time.sleep(np.random.uniform(2.0, 5.0))
            opciones.driver.find_element(By.XPATH, "//button[@class='dCJp8 afkep']").click()
            time.sleep(np.random.uniform(5.0, 8.0))                                        # Para evitar ser detectados, entre cada click habrá un tiempo random.
            opciones.driver.find_element(By.XPATH, "//button[@class='dCJp8 afkep']").click()
            time.sleep(np.random.uniform(2.0, 5.0))
        except:                                                                         # Volvemos a indicar la ubicación del botón, ya que se actualiza con cada click.
            pass
except:
    pass

# Tomar los nombres de los usuarios de los comentarios
users = opciones.driver.find_elements(By.XPATH, '//ul[@class="Mr508 "]')            # Busca en todos los elementos del DOM (//) todos los elementos con el tag <ul>, cuyo atributo "class" sea igual a "Mr508 "

file = open('users.txt','w')                                                                       # Se almacenará una lista o array con cada uno de los elementos buscados                           

for user in users:
    nick = user.find_element(By.XPATH, './/a[@class="sqdOP yWX7d     _8A5w5   ZIAjV "]').text
    file.write("@"+nick+"\n")
    print("@"+nick)

file.close()

print("Filtrando usuarios...")

file = open("users.txt", "r")
lineas = file.readlines() 
file.close()                        # Creamos una lista con cada una de sus lineas

file = open("users.txt","w")        
for linea in lineas:                # recorremos todas las lineas
    # miramos si el contenido de la linea es diferente a la linea a eliminar añadimos al final \n que es el salto de linea
    if linea!="@"+username+"\n":       # Si no es la linea que queremos eliminar, guardamos la linea en el archivo
        file.write(linea)
 
file.close()

# Eliminar duplicados
with open("users.txt", "r") as f_in:
   unicos = set(f_in.readlines())
with open("users.txt", "w") as f_out:
   f_out.write("".join(unicos))

# Guardar lista final
output = str(input("Ingrese el nombre del archivo de salida: "))
output = os.path.dirname(os.path.abspath(__file__)) + output

shutil.copy("users.txt", output)

print("Lista de usuarios creada!")

os.remove("users.txt")
opciones.driver.close()
opciones.driver.quit()

