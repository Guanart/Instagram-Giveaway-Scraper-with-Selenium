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
# Mis módulos
import login
import opciones

# Login
print("Loggeando...")
login.login()

# URL del sorteo
sorteo = input("Ingrese la URL del sorteo: ")
print("Cargando sorteo...")
opciones.driver.get(sorteo)

# Importar lista de usuarios
file = str(input("Ingrese el nombre de la lista de usuarios: "))
file = os.path.dirname(os.path.abspath(__file__)) + file
print("Importando nombres de usuarios...")

# Taggear a los usuarios
print("Ingrese el rango de líneas a taggear ([n1:n2])")
n1 = int(input("Ingrese la primer línea (n1): "))
n2 = int(input("Ingrese la última línea (n2): "))

with open(file, "r") as f:
    lineas = f.readlines()[n1:n2]

#text_area = opciones.driver.find_element(By.XPATH, '//textarea[@class="Ypffh"]')

# Para arrobar tres juntos:
# str(linea.rstrip('\n') + " " + linea.rstrip('\n')  + " " + linea.rstrip('\n'))

def comentar(lista):
    for comentario in lista:
        try:
            error = None
            error = opciones.wait.until(EC.presence_of_element_located((By.XPATH, '//p[@class="gxNyb"]'))).text
        except:
            pass
        
        if error is None:           # En lugar de usar "=", usamos is. También podemos usar "is not"
            try:
                time.sleep(np.random.uniform(3.0, 5.0))
                opciones.driver.find_element(By.XPATH, '//textarea[@class="Ypffh"]').click()
                time.sleep(np.random.uniform(3.5, 4.0))
                opciones.driver.find_element(By.XPATH, '//textarea[@class="Ypffh focus-visible"]').send_keys(comentario, Keys.ENTER)
                print(comentario)
                time.sleep(np.random.uniform(2.5, 4.0))
            except:
                pass
        else:
            print("No se pudo publicar el comentario. Pausando...")
            opciones.driver.refresh()
            time.sleep(np.random.uniform(300.0, 350.0))
            print("Reanudando...")

def taggear1(inicio, final):
    lista = []
    for i in range(inicio, final, 2):
        comentarios = lineas[0+i].rstrip('\n')
        lista.append(comentarios)
    comentar(lista)

def taggear2(inicio, final):
    lista = []
    for i in range(inicio, final, 2):
        comentarios = lineas[0+i].rstrip('\n') + " " + lineas[1+i].rstrip('\n')
        lista.append(comentarios)
    comentar(lista)
            
def taggear3(inicio, final):
    lista = []
    for i in range(inicio, final, 3):
        comentarios = lineas[0+i].rstrip('\n') + " " + lineas[1+i].rstrip('\n') + " " + lineas[2+i].rstrip('\n')
        lista.append(comentarios)
    comentar(lista)

tag_mode = input("Ingrese el número de usuarios a tagear por comentario: ")
print("Taggeando usuarios...")

if tag_mode == "1":
    taggear1(n1, n2)

if tag_mode == "2":
    taggear2(n1, n2)

if tag_mode == "3":
    taggear3(n1, n2)

#def borrar(n1, n2):
#    f = open(file, "r")
#    lineas = f.readlines()
#    f.close()
#    
#    f = open(file, "w")
#    
#    for i in range(n1, n2):
#        linea=lineas[i]
#        lineas.remove(linea)
#
#    for linea in lineas:
#        f.write(linea)
#    f.close()
#
#borrar(n1, n2)

#opciones.driver.close()
#opciones.driver.quit()