# Makefile

# Definir las rutas y nombres de los archivos
FEATURES_DIR = features
STEPS_FILE = steps/my_steps.py

# Definir el comando para ejecutar Behave
behave_command = behave --no-capture
behave_allure = behave -f allure_behave.formatter:AllureFormatter -o reports/
behave_xml = behave --junit --junit-directory ./report
allure = allure serve reports/

behave_chrome:
	@$(behave_command) 

behave_report:
	@$(behave_allure) 

behave_xml:
	@$(behave_xml) 	

allure:
	@$(allure)

#make behave_chrome
#make behave_report
#make behave_xml
#make allure