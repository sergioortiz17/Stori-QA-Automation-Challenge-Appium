# Stori Challenge Sergio Ortiz version MOBILE Appium
# STACK : Behave Python Cucumber-Gherkin POM
# Reporte Allure y xml junit

Link Video Ejecucion Appium 

https://drive.google.com/file/d/1clJtJlQ-6hSAWuenzBLh3neLCL0s79cA/view?usp=sharing

# Requerimientos y Configuracion de entorno
1. Python instalado https://www.python.org/
2. Administrador de paquetes pip (Verificas con pip --version)
3. pip install virtualenv (venv opcional-deseable -nice to have)
4. Instalacion allure report https://www.skill2lead.com/allure-report/allure-report-behave-allure-report-configuration.php
5. Instala Node.js desde https://nodejs.org/en/download/.
6. Abre una terminal y ejecuta el siguiente comando: npm install -g appium.
7. Instalar Appium Server Descarga La version estable 1.22.2 de Appium Server GUI desde https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4.
 instalando appium --version 1.22.2 en adelante
8. Opcional - Recomendable Instalar appium-doctor https://github.com/appium/appium-doctor  ya que indica si reconoce bien las variables de entorno desde tu venv o enviroment global
9. Instalar Node.js JDK y SDK.
10. Crea las variables de entorno JAVA_HOME y ANDROID_HOME con la ruta donde están instalados los archivos JDK y SDK respectivamente.
	Configura las variables de entorno de tu sistema
	- Windows tiene interfaz grafica para hacerlo
	- Linux (dependiendo de tu shell agregalas a tu file gedit ~/.zshrc o  ~/.bashrc y  update con su correspondiente para que tome el cambio )
		Ejemplo:
		export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
		export ANDROID_HOME=/home/sergioortiz/Android/Sdk
		export SDK_ROOT= /home/sergioortiz/Android/Sdk
	
11. Instala Android Studio para crear un Emulador
	Crea un emulador con la siguiente descripcion:
		Device: Pixel 4 XL API 31
		OS : Android 12.0 Google APIs | x86_64

# Uso

Para ejecutar las pruebas, se deben seguir los siguientes pasos:

1. Clonar el repositorio en tu máquina local.
2. Crear un entorno virtual e instala dependencias dentro con `pip install -r requirements.txt` en la raiz del proyecto (opcional deseable-nicetohave).
3. Levanta el servidor de Appium
4. Enciende el Emulador - Virtual Device Manager 
	Si instalaste el device de la configuracion no debes cambiar las capabilities por lo que queda igual:
	"appium:deviceName": "emulator64_x86_64_arm64"
5. Ejecutar prueba usando los comandos o sus shortcuts :
	
	Run sin logs solo viendo la interfaz grafica
	`behave`
    Run test viendo logs en consola
    `make behave_chrome` o `behave --no-capture`  
    Run y genera folder reports con formato de allure para levantar reporte html
    `make behave_report` o `behave -f allure_behave.formatter:AllureFormatter -o reports/` 
    Run y genera file con reporte xml
    `make behave_xml` o `behave --junit --junit-directory ./report`

# REPORTE
Para ver los reportes de Allure en la carpeta reports/ (despues de haberlo ejecutado con `make behave_report` o `behave -f allure_behave.formatter:AllureFormatter -o reports/`)ejecuta el siguiente comando en la carpeta raiz, para que levante el servidor y puedas verlo en un puerto local de tu browser  
    `make allure` o `allure serve reports/`

# Estructura
- Stori-QA-Automation-Challenge-Appium
    - app (applications.py init class)
    - configuration
        - config.py (Importante Capabilities)	
    - features
        - pages_Object
            - __init__.py
            - PracticePage.py   (POM)                                     
        - steps
            - __init__.py
            - AutomationPractice.py
        - test            
            - __init__.py
            - AutomationPractice.feature
        - enviroment.py (Hooks)       
    - support (Actions)
    - requirements.txt (contiene lista de dependencias)  
    - Makefile (rules shorcuts para scripts por consola)                  
    - reports (solo aparece si ejecutas `make behave_report`)

## Ayuda Extra con instalación del archivo requirements

Instala las dependencias necesarias para este proyecto, sigue los siguientes pasos:

1. Después de descargar el repositorio, abre tu IDE y selecciona la carpeta del proyecto para crear un entorno virtual de Python. Asegúrate de tener Python 3.11 o una versión superior instalada.
2. Crea una variable de entorno para el intérprete de Python actualizado. Copia la ruta absoluta de la variable de entorno hasta la carpeta "Scripts".
3. Abre una consola de comando y accede a la ruta copiada.
4. Ejecuta el siguiente comando para activar la variable de entorno:
`activate`
5. Una vez allí, ejecuta el siguiente comando para instalar todas las dependencias del proyecto:
`pip install -r requirements.txt`
6. Recuerda activar tu venv para correr los test

## Uso Appium con device fisico 
(Para ejecuciones sin pipeline ya que sin emular device ahorra recursos de computo)

Para ejecutar las pruebas, con device fisico se deben seguir los siguientes pasos:

1. Clonar el repositorio en tu máquina local.
2. Obtener Datos del Device desde ADB
   - Abrir consola CMD y tener el dispositivo físico conectado a la pc
   - Ejecutar el comando:
      `adb devices -l`
   - Se obtendría la data sobre el nombre del dispositivo como device-name    
3. Configurar archivo config.py el capabilities que lleva por nombre (**ANDROID_CONFIG**), ubicando el package y activity correspondiente al app y el cambio de nombre de device y version de OS Android:
	- Abir consola CMD en Windows o terminal en linux
	- Tener dispositivo físico con permisos de depurar USB conectado a la pc
	- Acceder desde el dispositivo físico al app
	- Correr el comando: 
		`adb shell "dumpsys window windows ! grep -E 'mCurrentFocus|mFocusedApp`
	- Sustraer el package y activity
	- Ingresar la información del package y activity donde corresponde dentro del archivo config.py
4. Modificar el archivo `config.py` con las rutas correspondientes al package, activity de la app a probar (OJO esto ya esta configurado en el repo para abrir app de google chrome)


