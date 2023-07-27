import os




class Datatest:
    URL = "http://localhost:4723/wd/hub"
    IMPLICIT_WAIT = 10
    
    # Sistema operativo a seleccionar, Aqui se define que tipo de sistema operativo se ejecutaran las pruebas (android, iOs)
    OS = "android"
    """
    # Rutas para acceder a la BD
    PATH_BD = os.path.abspath("resources/BD.xlsx")

    # Ruta para apk de navegador
    PATH_APK_BROWSER = os.path.abspath("resources/browser.apk")

    # Ruta para apk Assist Card
    PATH_APK_MYAC = os.path.abspath("resources/app.apk")

    # URL de proveedor de correos temporales
    MAIL_PROVIDER = "https://rahulshettyacademy.com/AutomationPractice/"
    """
    ##################### CONFIGURACION DE CAPABILITIES ########################################

    # Configuración para ejecutar pruebas en dispositivos Android
    ANDROID_CONFIG = {
        "platformName": "Android",
        "appium:platformVersion": "12",
        "appium:deviceName": "emulator64_x86_64_arm64",   # moto g30
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.android.chrome",
        "appium:appActivity": "com.google.android.apps.chrome.Main",
        #"app": f"{PATH_APK_MYAC}",
        "appium:grantPermissions": "true",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "resetKeyboard": True
    }

    # Configuración para ejecutar pruebas en dispositivos iOS
    IOS_CONFIG = {
        "platformName": "iOS",
        "automationName": "XCUITest",
        "deviceName": "iPhone 11",
        "platformVersion": "14.5",
        "app": "path/to/your/app", # Indicar la ruta de alocaion de la app AssistCard
        "noReset": True
    }



















































































