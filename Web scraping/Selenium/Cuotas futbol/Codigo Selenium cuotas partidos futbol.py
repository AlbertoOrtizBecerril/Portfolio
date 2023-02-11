from selenium import webdriver
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option("detach", True)
options.add_argument("--incognito")

website = 'https://www.wincomparator.com/es-es/cuotas/futbol/'
path = 'D:/chromedriver/chromedriver.exe' 

driver = webdriver.Chrome(path, chrome_options=options)

driver.get(website)
driver.implicitly_wait(3)

aceptar_condiciones = driver.find_element_by_xpath('//*[@id="logo-box"]/div[2]/a')
aceptar_condiciones.click()

driver.implicitly_wait(2)

fechas = driver.find_elements_by_xpath('//*[@id="list-wrapper"]/div[*]/div/div[1]/div[1]/div[1]/div/span')
lista_fechas = [fecha.text for fecha in fechas]

equipos_locales = driver.find_elements_by_xpath('//*[@id="list-wrapper"]/div[*]/div/div[1]/div[1]/a/div[1]/span')
lista_equipos_locales = [equipo_local.text for equipo_local in equipos_locales]

equipos_visitantes = driver.find_elements_by_xpath('//*[@id="list-wrapper"]/div[*]/div/div[1]/div[1]/a/div[3]/span')
lista_equipos_visitantes = [equipo_visitante.text for equipo_visitante in equipos_visitantes]

cuotas_uno = driver.find_elements_by_xpath('//*[@id="list-wrapper"]/div[*]/div/div[2]/div[1]/a[1]/span[1]')
lista_cuotas_uno = [cuota_uno.text for cuota_uno in cuotas_uno]

cuotas_x = driver.find_elements_by_xpath('//*[@id="list-wrapper"]/div[*]/div/div[2]/div[1]/a[2]/span[1]')
lista_cuotas_x = [cuota_x.text for cuota_x in cuotas_x]

cuotas_dos = driver.find_elements_by_xpath('//*[@id="list-wrapper"]/div[*]/div/div[2]/div[1]/a[3]/span[1]')
lista_cuotas_dos = [cuota_dos.text for cuota_dos in cuotas_dos]

df = pd.DataFrame({'Fecha': lista_fechas, 'Equipo local': lista_equipos_locales, 
                   'Equipo visitante': lista_equipos_visitantes, 'Cuota 1': lista_cuotas_uno, 
                   'Cuota X': lista_cuotas_x, 'Cuota 2': lista_cuotas_dos})

df.to_csv("partidos_dos.csv", index=True)

driver.quit()
