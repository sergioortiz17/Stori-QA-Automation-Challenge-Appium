import datetime
import subprocess
import time

from appium import webdriver
import allure
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
    WebDriverException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys

class BaseActions:

    def __init__(self, driver):
        self.driver = driver
        global act
        act = ActionChains(driver)

    @staticmethod
    def Tiempo(tie):
        time.sleep(tie)

    def closeDriver(self):
        self.driver.close()

    ######################### ACTION CHAINS #######################################################################
    def clickAction(self, by_tipo: By, selector: str, tiempo: float):

        try:
            val = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((by_tipo, selector)))
            act.click(val).perform()
            BaseActions.Tiempo(tiempo)
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def key_Up_Key_Down(self, by_tipo: By, selector: str, tecla: Keys, tiempo: float):

        try:
            val = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((by_tipo, selector)))
            act.click(val).perform()
            act.key_down(tecla).key_up(tecla).perform()
            act.key_down(tecla).key_up(tecla).perform()
            act.key_down(tecla).key_up(tecla).perform()
            act.key_down(tecla).key_up(tecla).perform()
            act.key_down(tecla).key_up(tecla).perform()
            act.key_down(tecla).key_up(tecla).perform()
            elemento_enfocado = self.driver.switch_to.active_element

            return elemento_enfocado


        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    ################################# TAP AND GESTURES ON SCREEN #################################################

    def tap_Screen(self, x, y, durationMiliSeconds):

        try:

            self.driver.execute_script('mobile: longClickGesture', {'x': x, 'y': y, 'duration': durationMiliSeconds})
            
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se hacia tap en las coordenadas " \
                          f": X: {x} ,  Y: {y}\n El Error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    ######################### SEARCH AND SEND, INPUTS; ELEMENTS; TEXT AND SELECTORS ################################

    def find_element(self, by_tipo: By, selector: str):
        try:
            val = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((by_tipo, selector)))
            return val
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento {selector} de tipo {by_tipo}\n El Error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento {selector} de tipo {by_tipo}\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"

    def clickCheckCapchat(self):
        try:
            result = False
            time.sleep(1)
            elements = None
            elements = self.driver.find_elements(By.CLASS_NAME,
                                                 "android.widget.CheckBox")  
            for ele in elements: 
                if ele.text == "No soy un robot":
                    print(f"Se encontro el capchat")
                    elements[elements.index(ele)].click()  
                    result = True
                    break
            if result is False:
                print("No hay capchat que validar")
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se" \
                          f"buscaba algun capchat en pantalla\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró ningun capchat en pantalla\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar ningun capchat en pantalla\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido al buscar algun capchat en pantalla: {ex}"

    def keyboard_Hide(self):

        try:
            self.driver.hide_keyboard()
            print("Se realizó la acción de ocultar el teclado")
        except Exception as ex:
            assert False, f"Error desconocido al intentar ocultar el teclado: {ex}"


#################################### ALLURE SCREENCSHOT ##############################################

    def screenshot(self, nombre=str):

        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.PNG)
        print("Imagen capturada")

    def uploadFile(self, tipo=By, selector=str, ruta=str):
        try:
            val = self.driver.find_element(tipo, selector)
            val.send_keys(ruta)
            print("\n Elemento Cargado -> {} ".format(selector))
        except Exception as ex:
            assert False, f"No se pudo subir el archivo {ruta}\n El error es: {ex}"


    def open_url(self, url):
        try:
            self.driver.get(url)  # Utiliza el método get() del WebDriver para abrir la URL

        except Exception as ex:
            assert False, f"No se pudo abrir la URL {url}\nEl error es: {ex}"

    def send_Text_Input(self, by_tipo: By, selector: str, texto: str, tiempo: float):



        try:
            ele = None
            ele = self.driver.find_element(by_tipo, selector)
            # Limpiar campo y enviar texto
            ele.clear()
            ele.send_keys(texto)
            BaseActions.Tiempo(tiempo)
            print(f"Cargado el texto {texto} correctamente")
        except NoSuchElementException as ex:
            assert False, f"No se pudo enviar el texto en el input debido a que\n" \
                          f"no encontró el elemento con el selector '{selector}'  de tipo: '{by_tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se pudo enviar el texto en el input debido a que\n" \
                          f"no se puede interactuar con el elemento '{selector}' de tipo: '{by_tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se pudo enviar el texto en el input debido a que\n" \
                          f"el Tiempo de espera fue excedido para encontrar el elemento '{selector}' de tipo: '{by_tipo}" \
                          f"'\n Error Log: {ex.msg}"
        except Exception as ex:
            assert False, f"Error Desconocido al intentar evniar texto en el input con en el elemento: {selector} de tipo {by_tipo}" \
                          f"\n Error Log : {ex.args}"
                   
########################### SCROOLS ##############################################


    def scroll_derecha(self):
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] * 0.2  # Punto inicial (20% desde el borde izquierdo)
        end_x = window_size['width'] * 0.8    # Punto final (80% desde el borde izquierdo)
        y = window_size['height'] * 0.5       # Altura media de la pantalla

        action = TouchAction(self.driver)
        action.press(x=start_x, y=y).wait(1000).move_to(x=end_x, y=y).release().perform()

    def scroll_izquierda(self):
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] * 0.6 # Punto inicial (80% desde el borde izquierdo)
        end_x = window_size['width'] * 0.4     # Punto final (20% desde el borde izquierdo)
        y = window_size['height'] * 0.5        # Altura media de la pantalla

        action = TouchAction(self.driver)
        action.press(x=start_x, y=y).wait(1000).move_to(x=end_x, y=y).release().perform()
     
    def scroll_down(self):
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] * 0.5   # Coordenada X central de la pantalla
        start_y = window_size['height'] * 0.55  # Punto inicial (55% desde la parte superior)

        end_y = window_size['height'] * 0.45   # Punto final (45% desde la parte superior)

        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).wait(1000).move_to(x=start_x, y=end_y).release().perform()

    def scroll_down_search(self):
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] * 0.5   # Coordenada X central de la pantalla
        start_y = window_size['height'] * 0.55  # Punto inicial (55% desde la parte superior)
        end_y = window_size['height'] * 0.15   # Punto final (15% desde la parte superior)

        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).wait(1000).move_to(x=start_x, y=end_y).release().perform()

    def scroll_up(self):
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] * 0.5   # Coordenada X central de la pantalla
        start_y = window_size['height'] * 0.45  # Punto inicial (45% desde la parte superior)

        end_y = window_size['height'] * 0.55   # Punto final (55% desde la parte superior)

        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).wait(1000).move_to(x=start_x, y=end_y).release().perform()


    def get_element_text(self, element_xpath):
        try:
            # Localizar el elemento por su XPath
            element = self.driver.find_element(By.XPATH, element_xpath)
            
            # Obtener el texto del elemento
            element_text = element.text
            return element_text
        except:
            return None
      
    def get_path(self, row:int , col:int)->str:
        base_xpath = (
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
            "android.widget.FrameLayout/android.widget.FrameLayout/"
            "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
            "android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/"
            "android.view.View/android.widget.GridView"
            "/android.view.View[{row}]/android.view.View[{col}]"
        )
        return base_xpath.format(row=row, col=col)

    def get_path_position(self, row:int , col:int)->str:
        base_xpath_position = (
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
        "android.widget.FrameLayout/android.widget.FrameLayout/"
        "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
        "android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/"
        "android.view.View[2]/android.widget.GridView/"
        "android.view.View[{row}]/android.view.View[{col}]"
        )
        return base_xpath_position.format(row=row, col=col)

    def get_path_iframe(self, row:int )->str:

        base_xpath_iframe = ( 
         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
         "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
         "android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/"
         "android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/"
         "android.view.View/android.view.View/android.view.View/android.view.View[2]/"
         "android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[[{row}]]"
        ) 

        return base_xpath_iframe.format(row=row)

    def guardar_en_txt(self, nombre_archivo, datos):
        
        # Abre el archivo en modo escritura ('w')
        with open(nombre_archivo, "w") as archivo:
            for dato in datos:
                archivo.write(str(dato) + "\n")            


    def verifyRegraan(self):

        try:
            result = False
            time.sleep(1)
            elements = None

            elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                 "div.container")  
            for ele in elements:  
                if ele.text == "30 DAY":
                    print(f"Se encontro Mensaje de Garantia")
                    elements[elements.index(ele)].click()  
                    result = True
                    break
            if result is False:
                print("No se encontro Mensaje de Garantia")
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se" \
                          f"buscaba algun Msj de Rembolso en pantalla\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró ningun Msj de Rembolso en pantalla\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No hay Msj de Rembolso en pantalla para interactuar\n El error es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido al buscar algun Msj de Rembolso en pantalla: {ex}"

    def switch_to_iframe_by_xpath(self):
        try:
            iframe_element = self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[2]")
            self.driver.switch_to.frame(iframe_element)
            print("Cambió al iframe")
        except Exception as e:
            print("Error al cambiar al iframe:", e)

    def expand_iframe_to_full_screen(self):
        try:
            iframe_element = self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[2]")
            window_size = self.driver.get_window_size()

            
            self.driver.execute_script(
                "arguments[0].style.width = '{}px';".format(window_size['width']), iframe_element)
            self.driver.execute_script(
                "arguments[0].style.height = '{}px';".format(window_size['height']), iframe_element)

            print("El iframe se ha expandido a toda la pantalla.")
        except Exception as e:
            print("Error al expandir el iframe:", e)



    def findElementIsVisibleBySelector(self, by_tipo: By, selector: str):

        try:
            result = False
            element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located
                                                          ((by_tipo, selector)))
            if element.is_displayed():
                result = True
                print(f"Se encontro en pantalla el elemento: {selector} de tipo {by_tipo}")
            return result
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaba el " \
                          f"elemento: {selector} de tipo {by_tipo}\n El error es: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontró el elemento: {selector} de tipo {by_tipo}\n El error es: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con el elemento:" \
                          f" {selector} de tipo {by_tipo}\n El erro es: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"


    def scroll_down_search_small(self):
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] * 0.5   
        start_y = window_size['height'] * 0.55 

        end_y = window_size['height'] * 0.25  

        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).wait(1000).move_to(x=start_x, y=end_y).release().perform()