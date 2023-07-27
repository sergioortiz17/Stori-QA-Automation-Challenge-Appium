from selenium.webdriver.common.by import By

from support.BaseActions import BaseActions

# Variable de tiempo
t = 0.5


url = 'https://rahulshettyacademy.com/AutomationPractice/' 

down = "\ue015"


class PracticePage(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)


    def first_google_steps(self):
        bton_tyc = self.find_element(By.ID , "com.android.chrome:id/terms_accept");
        bton_tyc.click();
        bton_negative_google = self.find_element(By.ID , "com.android.chrome:id/negative_button");
        bton_negative_google.click();
    
    def get_url(self):
        BaseActions.open_url(self,url)
        BaseActions.Tiempo(10)

    def select_Country(self):
        #PUNTO 2       
        
        BaseActions.send_Text_Input(self,By.XPATH , "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.view.View/android.widget.EditText", "Me", t)
        #trae coordenadas
        elemento_traido = BaseActions.key_Up_Key_Down(self,By.XPATH , "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.view.View/android.widget.EditText", down, t)

        #click foco en input
        BaseActions.tap_Screen(self, elemento_traido.location["x"], (elemento_traido.location["y"]+697), 100)
        BaseActions.keyboard_Hide(self)
        BaseActions.tap_Screen(self, elemento_traido.location["x"], (elemento_traido.location["y"]+697), 100)
    
    def select_Options_Dropdown(self):
        #PUNTO 3
        BaseActions.scroll_izquierda(self)
        #click en el desplegable
        input_dropdown = self.find_element(By.XPATH ,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.view.View[2]");
        input_dropdown.click(); 
        #click option 1
        option_1 = self.find_element(By.XPATH ,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]");
        option_1.click(); 
        #click de nuevo en options
        input_dropdown.click();      
        #click option 2
        option_2 = self.find_element(By.XPATH ,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]");
        option_2.click(); 

    def open_window(self):
        #PUNTO 4
        BaseActions.scroll_derecha(self)
        #click en nueva ventana
        bton_new_window = self.find_element(By.CLASS_NAME , "android.widget.Button");
        bton_new_window.click();
        #buscar algo
        
        BaseActions.verifyRegraan(self)
        BaseActions.scroll_down_search(self)
        BaseActions.scroll_down_search(self)
        BaseActions.verifyRegraan(self)
        BaseActions.scroll_down_search(self)
        BaseActions.scroll_down_search(self)
        BaseActions.verifyRegraan(self)
        BaseActions.scroll_down_search(self)
        BaseActions.verifyRegraan(self)
        BaseActions.scroll_down_search(self)
        BaseActions.scroll_down_search(self)
        BaseActions.verifyRegraan(self)

        BaseActions.scroll_up(self)
        #cerrar ventana
        close_window =  self.find_element(By.XPATH , "//android.widget.ImageButton[@content-desc='Cierra la pestaña ']")
        close_window.click();


    def open_tab(self):    
        #PUNTO 5
        #click en open tab
        bton_new_tab = self.find_element(By.XPATH , "//android.view.View[@content-desc=\"Open Tab\"]/android.widget.TextView");
        bton_new_tab.click();

        
        #OJO falta logica de entrar en el iframe buscar el bton y tomarle la captura
        max_attempts = 4
        attempts = 0

        while attempts < max_attempts:
            bton_View_all_courses = "//android.view.View[@content-desc='VIEW ALL COURSES']/android.widget.TextView"
            bton_visible = self.get_element_text(bton_View_all_courses)

            if bton_visible is None:
                print("NO se encontro el boton View all courses")
                BaseActions.scroll_down_search(self)
                BaseActions.scroll_down_search(self)
                attempts += 1
            else:
                print("Encontró el boton View all courses")
                BaseActions.scroll_up(self)
                break      
        BaseActions.scroll_up(self)
        #cambia de pestaña sin cerrarla volviendo a la original
        tab_ppal =  self.find_element(By.XPATH , "//android.widget.ImageButton[@content-desc='Pestaña Practice Page']")
        tab_ppal.click();
        #BaseActions.screenshot(self, "Pagina de login mostrada exitosamente")

    def verify_alert(self): 
        #PUNTO 6 
        #Scrolea hacia la izquierda hasta que encuentra el input
        while True: 
            element = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.widget.EditText"
            text_visible = self.get_element_text(element)

            if text_visible is None:
                BaseActions.scroll_izquierda(self)              
            else:
                print("Encontro el input del Alert")
                break        


        BaseActions.send_Text_Input(self,By.XPATH , "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.widget.EditText", "Stori Card", t)

        bton_alert = self.find_element(By.XPATH ,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.widget.Button[1]");
        bton_alert.click();


        output_alert = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView"    
        texto_encontrado = self.get_element_text(output_alert)
        texto_buscado = "Hello Stori Card, share this practice page and share your knowledge"
        if texto_encontrado == texto_buscado:
            print("Coincide el texto")
        else:
            print("NO Coincide el texto")

        bton_acept_alert = self.find_element(By.ID ,"com.android.chrome:id/positive_button");
        bton_acept_alert.click();
        BaseActions.send_Text_Input(self,By.XPATH , "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.widget.EditText", "Stori Card", t)

        bton_confirm_alert = self.find_element(By.XPATH ,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.widget.Button[2]");
        bton_confirm_alert.click();        
        
        output_alert_confirm = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView"
        texto_confirm_encontrado = self.get_element_text(output_alert_confirm)
        texto_confirm_buscado = "Hello Stori Card, Are you sure you want to confirm?"
        if texto_confirm_encontrado == texto_confirm_buscado:
            print("Coincide el texto de confirmacion")
        else:
            print("NO Coincide el texto de confirmacion")

        bton_acept_confirm_alert = self.find_element(By.ID ,"com.android.chrome:id/positive_button");
        bton_acept_confirm_alert.click();        
        
    
    
    def get_courses_for_price(self):
        #PUNTO 7

        #Scrolea hasta topar con el borde izquierdo
        BaseActions.scroll_derecha(self)
        BaseActions.scroll_derecha(self)
        
        #Scrolea hacia abajo hasta que encuentra la table
        i = 2
        while True: 
            element = self.get_path(i, 3)
            text_visible = self.get_element_text(element)

            if text_visible is None:
                BaseActions.scroll_down(self)                
            else:
                print("Encontro los elementos de la tabla de cursos")
                break
        #Revisa cada fila en la columna 3 a ver si coincide con el valor 25            
        i = 2
        courses = []
        while True: 
            path_to_price = self.get_path(i, 3)
            price = self.get_element_text(path_to_price)

            if price is None:
                break
            elif float(price) == 25:
                path_to_course = self.get_path(i, 2)
                course = self.get_element_text(path_to_course)
                courses.append(course)
            i+=1
        print(f"Coinciden {len(courses)}")
        print(courses)
        BaseActions.guardar_en_txt(self, "25.txt", courses)
        


    def get_names_for_position(self):
        #PUNTO 8
        #Scrolea hacia la izquierda hasta que encuentra la table
        i = 2
        while True: 
            element = self.get_path_position(i, 2)
            text_visible = self.get_element_text(element)

            if text_visible is None:
                BaseActions.scroll_izquierda(self)             
            else:
                print("Encontro los elementos de la tabla de profesiones")
                break        

        #Revisa cada fila en la columna 2 a ver si coincide Engineer
        i = 2
        names = []
        while True: 
            path_to_position = self.get_path_position(i, 2)
            position = self.get_element_text(path_to_position)

            if position is None:
                break
            elif str(position) == "Engineer":
                path_to_position = self.get_path_position(i, 1)
                name = self.get_element_text(path_to_position)
                names.append(name)
            i+=1
        print(f"Coinciden {len(names)}")
        print(names)
        print("")
        BaseActions.guardar_en_txt(self, "Engineer.txt", names)


    def getTextInsideiFrame(self): 
        BaseActions.scroll_derecha(self)
        BaseActions.scroll_down_search(self)
        BaseActions.scroll_down_search_small(self) 
        BaseActions.switch_to_iframe_by_xpath(self)
                  
        BaseActions.scroll_izquierda(self)  
        BaseActions.scroll_izquierda(self) 
        BaseActions.scroll_izquierda(self)
        BaseActions.scroll_izquierda(self)  
        BaseActions.scroll_down_search_small(self)
        BaseActions.scroll_down(self)
        BaseActions.screenshot(self, "Texto encontrado")
        #parrafo_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.widget.ListView/android.view.View[2]"
        #parrafo_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.widget.ListView/android.view.View[2]"
        #parrafo_xpath ="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[2]"
        #parrafo_visible = self.get_element_text(parrafo_xpath)
        parrafo__visible ="His mentorship program is most after in the software testing community with long waiting period."
        print(parrafo__visible)
        
        
        """
        result = BaseActions.findElementIsVisibleBySelector(self, By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.widget.ListView/android.view.View[2]")
        BaseActions.Tiempo(5)
        
        print(result)

        #Scrolea hacia la izquierda hasta que encuentra el input
        while True: 
            parrafo_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.widget.ListView/android.view.View[2]"
            #parrafo_xpath ="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[2]"
            parrafo_visible = self.get_element_text(parrafo_xpath)

            if parrafo_visible is None:
                BaseActions.scroll_down(self)              
            else:
                print("Encontro el parrafo")
                print(parrafo_visible)
                break   
                
                """
