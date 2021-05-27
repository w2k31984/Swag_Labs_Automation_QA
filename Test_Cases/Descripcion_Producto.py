##Test Automatizado para caso de prueba de ver la descripcion de un producto al seleccionarlo
#retornar a pantalla de productos.
import time
import HtmlTestRunner
import unittest
from selenium import webdriver

class myTestProductDescription(unittest.TestCase):

    def testProductDescription(self):
        driver = webdriver.Chrome(executable_path=r'C:\\Users\\cristian_parada\\Desktop\\Automatizacion_Test_Cases_Ecommerce\\chromedriver.exe')
        driver.get('https://www.saucedemo.com/')
        time.sleep(2)
        usuario = driver.find_element_by_id('user-name')
        usuario.clear()
        usuario.send_keys('standard_user')


        contrasena = driver.find_element_by_id('password')
        contrasena.clear()
        contrasena.send_keys('secret_sauce')
        time.sleep(3)

        driver.find_element_by_id('login-button').click()
        time.sleep(2)

#Dando click en un producto para ver su descripcion.
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div').click()
        time.sleep(2)
#Regresar a pagina de todos los productos dando click a boton.
        driver.find_element_by_id('back-to-products').click()
        time.sleep(2)
        driver.stop_client()
        driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Automatizacion_Test_Cases_Ecommerce\Reports'))