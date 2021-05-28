import time
import HtmlTestRunner
import unittest
from selenium import webdriver

class myTestRemoveProductToCart(unittest.TestCase):

    def testRemoverProductoCarrito(self):
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

#Seleccionando productos en pantalla de productos a carrito de compras (Mochila)
        driver.find_element_by_id('add-to-cart-sauce-labs-backpack').click()
        time.sleep(2)
#Seleccionando productos en pantalla de productos a carrito de compras (Fleece Jacket)
        driver.find_element_by_id('add-to-cart-sauce-labs-fleece-jacket').click()
        time.sleep(2)
# Seleccionando productos en pantalla de productos a carrito de compras (Bolt T-Shirt)
        driver.find_element_by_id('add-to-cart-sauce-labs-bolt-t-shirt').click()
        time.sleep(2)
#Revisando en carrito de compra los productos seleccionados.
        driver.find_element_by_id('shopping_cart_container').click()
        time.sleep(5)
#Retornar a pantalla de productos dando click a boton
        driver.find_element_by_id('continue-shopping').click()
        time.sleep(2)
#Removiendo producto dando click a boton de remover en el producto (Mochila)
        driver.find_element_by_id('remove-sauce-labs-backpack').click()
        time.sleep(2)
#Revisando en carrito de compra que no aparezca el producto seleccionado.
        driver.find_element_by_id('shopping_cart_container').click()
        time.sleep(2)
        driver.stop_client()
        driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Automatizacion_Test_Cases_Ecommerce\Reports'))
