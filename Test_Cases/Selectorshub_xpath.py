import time
import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class testSelectorsHubXpath(unittest.TestCase):

    def testSelectorsHubByXpath(self):
        driver = webdriver.Chrome(executable_path=r'C:\\Users\\cristian_parada\\Desktop\\Automatizacion_Test_Cases_Ecommerce\\chromedriver.exe')
        driver.get('https://www.saucedemo.com/')
        time.sleep(3)
    #Test para comprobar la efectividad de SelectorsHub con xpath herramienta desarrollada en navegador para QA
        #Test con login de usuario.
        usuario = driver.find_element_by_xpath("//input[@id='user-name']")
        usuario.clear()
        usuario.send_keys('standard_user')
        time.sleep(2)
        contrasena = driver.find_element_by_xpath("//input[@id='password']")
        contrasena.clear()
        contrasena.send_keys('secret_sauce')
        time.sleep(3)

        driver.find_element_by_xpath("//input[@id='login-button']").click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Automatizacion_Test_Cases_Ecommerce\Reports'))