import time
import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class myTestAddToCart(unittest.TestCase):

    def testAddToCart(self):
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

#Agregando producto a carrito de compras dando click a boton (Producto Mochila)
        driver.find_element_by_id('add-to-cart-sauce-labs-backpack').click()
        time.sleep(2)
#Realizar Scroll en la pagina para ver que se elige el otro producto
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
#Agregando otro producto a carrito de compras dando click a boton (T-Shirt Roja)
        driver.find_element_by_id('add-to-cart-test.allthethings()-t-shirt-(red)').click()
        time.sleep(3)
# Realizar Scroll en la pagina para regresar arriba
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        #driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(4)
#Verificar el carrito de compras con productos seleccionados dando click a icono de carrito de compras.
        driver.find_element_by_id('shopping_cart_container').click()
        time.sleep(3)
#Retornar a pantalla de productos dando click a boton
        driver.find_element_by_id('continue-shopping').click()
        time.sleep(2)
        driver.stop_client()
        driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Automatizacion_Test_Cases_Ecommerce\Reports'))
