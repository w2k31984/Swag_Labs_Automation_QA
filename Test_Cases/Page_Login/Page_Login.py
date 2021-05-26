#Test Automatizado para caso de prueba de ingreso a login
import time
import unittest
import HtmlTestRunner
from selenium import webdriver

class myTestWeb(unittest.TestCase):

    def testPageLogin(self):
        driver = webdriver.Chrome(executable_path=r'C:\\Users\\cristian_parada\\Desktop\\Automatizacion_Test_Cases_Ecommerce\\chromedriver.exe')
#Ingresamos al sitio web
        driver.get('https://www.saucedemo.com/')
        time.sleep(2)
#Ingresamos el usuario
        usuario = driver.find_element_by_id('user-name')
        usuario.clear()
        usuario.send_keys('standard_user')

#Ingresando la credencial
        contrasena = driver.find_element_by_id('password')
        contrasena.clear()
        contrasena.send_keys('secret_sauce')
        time.sleep(3)
#Dando click a boton Login
        driver.find_element_by_id('login-button').click()
        time.sleep(3)
        driver.stop_client()
        driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Automatizacion_Test_Cases_Ecommerce\Reports'))