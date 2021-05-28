import time
import HtmlTestRunner
import unittest
from selenium import webdriver

class myTestOrderByAlphabetDescending(unittest.TestCase):

    def testOrderByAlphabetDescending(self):
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

#Dando click al objeto clasificar contenido por.
        driver.find_element_by_class_name('product_sort_container').click()
        time.sleep(4)

#Seleccionando que clasifique por orden alfabeto descendente.
        driver.find_element_by_xpath('//*[@id="header_container"]/div[2]/div[2]/span/select/option[2]').click()
        time.sleep(7)
        driver.stop_client()
        driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Automatizacion_Test_Cases_Ecommerce\Reports'))
