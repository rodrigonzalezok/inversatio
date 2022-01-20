from os import system
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
import urllib3
import time
from time import sleep
from urllib import request
import requests
#Generamos el browser
browser = webdriver.Chrome(executable_path="agregar ruta del driver")
print(">>> Google Chrome.")
# Logueo
email = '' 
pas = ''
# Maximiza tamaño de pantalla
browser.maximize_window()
# Carga de la pagina
browser.get("https://www.bullmarketbrokers.com/")
# esperamos a que no se vea el aviso de cargando
WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
# clic en el botón ingresar
browser.find_element(By.LINK_TEXT, "Ingresar").click()
print("Clic en ingresar.")
# Esperamos a que se vea el boton de login del formulario 
WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "btn_login_ok")))
browser.find_element(By.ID, "txt_modal_login_idNumber").send_keys(email)
browser.find_element(By.ID, "txt_modal_login_password").send_keys(pas)
print("Cargamos los datos en el formulario.")
# Clic en el botón de login
browser.find_element(By.ID, "btn_login_ok").click()
print("Click en login.")
# Clic en el botón de Cotizaciones
WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
WebDriverWait(browser, 30000).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, "home-logged")))
time.sleep(2)
# Generamos el contador
contador = 0
while(True):
    browser.find_element_by_link_text("COTIZACIONES").click()
    # Extraemos la tabla del Panel Lider
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]/tr[21]")))
    tabla = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r = tabla.text
    pl = r.split()
    # Click en el botón ACCIONES
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[1]/span").click()
    # Click en el botón Panel General
    WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "a_stock_panel")))
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[1]/ul/li[2]/a").click()
    # Extraemos la tabla del Panel General
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla1 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r1 = tabla1.text
    pg = r1.split()
    # Click en el botón BONOS
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[3]/span").click()
    # Click en el botón TODOS LOS BONOS
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[3]/ul/li[1]/a").click()
    # Extraemos la tabla de Bonos
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla2 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r2 = tabla2.text
    bonos = r2.split()
    # Click en el botón CEDEARS
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[5]/a").click()
    # Extraemos la tabla de CEDEARS
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla3 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r3 = tabla3.text
    cedear = r3.split()
    # Click en el botón MERCADOS INTERNACIONALES
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[8]/a").click()
    # Extraemos la tabla de Mercados Internacionales
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla4 = browser.find_element_by_id('div_stockPricesUSA_result')
    r4 = tabla4.text
    mercadosinternacionales = r4.split()
    # Click en el botón OPCIONES
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[2]/a").click()
    # Extraemos la tabla de Opciones
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla5 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r5 = tabla5.text
    opciones = r5.split()
    # Click en el botón ROFEX
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[6]/span").click()
    # Click en el botón FUTUROS ROFEX
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[6]/ul/li[1]/a").click()
    # Extraemos la tabla de Futuros Rofex
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla6 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r6 = tabla6.text
    futurosrofex = r6.split()
    # Click en el botón ROFEX
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[6]/span").click()
    # Click en el botón OPCIONES ROFEX
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[6]/ul/li[2]/a").click()
    # Extraemos la tabla de Opciones Rofex
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla7 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r7 = tabla7.text
    opcionesrofex = r7.split()
    # Click en el botón LETRAS
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[4]/span").click()
    # Click en el botón LETRAS EN PESOS
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[4]/ul/li[1]/a").click()
    # Extraemos la tabla de Letras en Pesos
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla8 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r8 = tabla8.text
    letrasenpesos = r8.split()
    # Click en el botón LETRAS
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[4]/span").click()
    # Click en el botón LETRAS EN DÓLARES
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[4]/ul/li[2]/a").click()
    # Extraemos la tabla de Letras en Dólares
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla9 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r9 = tabla9.text
    letrasendolares = r9.split()
    # Click en el botón CAUCIONES
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/nav[1]/div[2]/ul/li[10]/a").click()
    # Extraemos la tabla de Cauciones
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "loading")))
    WebDriverWait(browser, 30000).until_not(expected_conditions.visibility_of_element_located((By.ID, "custom_loader")))
    time.sleep(1)
    tabla10 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div[1]/section/table/tbody[1]')
    r10 = tabla10.text
    cauciones = r10.split()
    # Extraemos tabla de Mercado
    WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "history")))
    tabla11 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[2]/div[1]/div/table/tbody')
    r11 = tabla11.text
    mercado = r11.split()

    urlpl = "http://rodrigonzalez.com.ar/datos/datospl.php?base"
    datospl = {'datospl': str(pl)}
    enviarpl = requests.post(urlpl, data = datospl)
    urlpg = "http://rodrigonzalez.com.ar/datos/datospg.php?base"
    datospg = {'datospg': str(pg)}
    enviarpg = requests.post(urlpg, data = datospg)
    urlbonos = "http://rodrigonzalez.com.ar/datos/datosbonos.php?base"
    datosbonos = {'datosbonos': str(bonos)}
    enviarbonos = requests.post(urlbonos, data = datosbonos)
    urlcedear = "http://rodrigonzalez.com.ar/datos/datoscedear.php?base"
    datoscedear = {'datoscedear': str(cedear)}
    enviarcedear = requests.post(urlcedear, data = datoscedear)
    urlmercadosinternacionales = "http://rodrigonzalez.com.ar/datos/datosmercadosinternacionales.php?base"
    datosmercadosinternacionales = {'datosmercadosinternacionales': str(mercadosinternacionales)}
    enviarmercadosinternacionales = requests.post(urlmercadosinternacionales, data = datosmercadosinternacionales)
    urlopciones = "http://rodrigonzalez.com.ar/datos/datosopciones.php?base"
    datosopciones = {'datosopciones': str(opciones)}
    enviaropciones = requests.post(urlopciones, data = datosopciones)
    urlfuturosrofex = "http://rodrigonzalez.com.ar/datos/datosfuturosrofex.php?base"
    datosfuturosrofex = {'datosfuturosrofex': str(futurosrofex)}
    enviarfuturosrofex = requests.post(urlfuturosrofex, data = datosfuturosrofex)
    urlopcionesrofex = "http://rodrigonzalez.com.ar/datos/datosopcionesrofex.php?base"
    datosopcionesrofex = {'datosopcionesrofex': str(opcionesrofex)}
    enviaropcionesrofex = requests.post(urlopcionesrofex, data = datosopcionesrofex)
    urlletrasenpesos = "http://rodrigonzalez.com.ar/datos/datosletrasenpesos.php?base"
    datosletrasenpesos = {'datosletrasenpesos': str(letrasenpesos)}
    enviarletrasenpesos = requests.post(urlletrasenpesos, data = datosletrasenpesos)
    urlletrasendolares = "http://rodrigonzalez.com.ar/datos/datosletrasendolares.php?base"
    datosletrasendolares = {'datosletrasendolares': str(letrasendolares)}
    enviarletrasendolares = requests.post(urlletrasendolares, data = datosletrasendolares)
    urlcauciones = "http://rodrigonzalez.com.ar/datos/datoscauciones.php?base"
    datoscauciones = {'datoscauciones': str(cauciones)}
    enviarcauciones = requests.post(urlcauciones, data = datoscauciones)
    urlmercado = "http://rodrigonzalez.com.ar/datos/datosmercado.php?base"
    datosmercado = {'datosmercado': str(mercado)}
    enviarmercado = requests.post(urlmercado, data = datosmercado)
    system('cls')
    contador+=1
    print("Enviamos los datos:",contador,"veces")
time.sleep(5000)