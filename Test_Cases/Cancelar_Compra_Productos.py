import time
import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class myTestcheckoutProducts(unittest.TestCase):

    def testCheckoutProducts(self):
        driver: WebDriver = webdriver.Chrome(executable_path=r'C:\\Users\\cristian_parada\\Desktop\\Automatizacion_Test_Cases_Ecommerce\\chromedriver.exe')
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

    # Agregando producto a carrito de compras dando click a boton (Producto Mochila)
        driver.find_element_by_id('add-to-cart-sauce-labs-backpack').click()
        time.sleep(2)
    # Realizar Scroll en la pagina para ver que se elige el otro producto
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
    # Agregando producto a carrito de compras dando click a boton (T-Shirt Roja)
        driver.find_element_by_id('add-to-cart-test.allthethings()-t-shirt-(red)').click()
        time.sleep(3)
    # Agregando producto a carrito de compras dando click a boton (Bike Light)
        driver.find_element_by_id('add-to-cart-sauce-labs-bike-light').click()
        time.sleep(3)
    # Verificar el carrito de compras con productos seleccionados dando click a icono de carrito de compras.
        driver.find_element_by_id('shopping_cart_container').click()
        time.sleep(3)
    # Realizar Scroll en la pagina para ver boton de ckeckout
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
    #Dando click al boton de ckeckout para continuar el proceso de venta.
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/button[2]').click()
        time.sleep(3)
    #Llenando datos del formulario con datos de usuario.

    #Ingresando Nombre del usuario.
        # Ingresando la credencial
        nombre = driver.find_element_by_id('first-name')
        nombre.clear()
        nombre.send_keys('Cristian')
        time.sleep(3)
    # Ingresando Apellido del usuario.
        apellido = driver.find_element_by_id('last-name')
        apellido.clear()
        apellido.send_keys('Parada')
        time.sleep(3)
    #Ingresando ZIP/POSTAL Code.
        zipcode = driver.find_element_by_id('postal-code')
        zipcode.clear()
        zipcode.send_keys('24060/Blacksburg, VA')
        time.sleep(3)
    # Realizar Scroll en la pagina para ver boton de ckeckout
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
    #Boton de Continuar la compra.
        driver.find_element_by_name('continue').click()
        time.sleep(4)
    # Realizar Scroll en la pagina para ver boton de ckeckout
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
    #Boton de Cancelar
        driver.find_element_by_id('cancel').click()
        time.sleep(4)
        driver.stop_client()
        driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Automatizacion_Test_Cases_Ecommerce\Reports'))