from behave import *
from app.application import Application


@given(u'I initialize Google')
def step_impl(context):
    try:
        context.application = Application(context.driver)
    except Exception as ex:
        assert False, f"Fallo el step al Inicializar la aplicacion Assist Card\n Motivo del Error: {ex}"

@when(u'First Google steps')
def step_impl(context):
    try:
        context.application.PracticePage.first_google_steps()
    except Exception as ex:
        assert False, f"Fallo el step al confirmar que se muestre la pagina inicial de bienvenida\n Motivo del Error: {ex}"

@when(u'I go to the url of the Automation Practice')
def step_impl(context):
    try:
        context.application.PracticePage.get_url()
    except Exception as ex:
        assert False, f"Fallo el step al confirmar que se muestre la pagina inicial de bienvenida\n Motivo del Error: {ex}"

@when(u'Select country automatically completing with your two initials')
def step_impl(context):
    try:
        context.application.PracticePage.select_Country()
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"
        
@when(u'Select Option 1 and Option 2 in the dropdown')
def step_impl(context):
    try:
        context.application.PracticePage.select_Options_Dropdown()
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"    

@when(u'Verify money back guarantee in qaclickacademy')
def step_impl(context):
    try:
        context.application.PracticePage.open_window()
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"    

@when(u'Tab control and button screenshot')
def step_impl(context):
    try:
        context.application.PracticePage.open_tab() #posible improve para iframePage and QaAcademyPage
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"  
        
@when(u'Send your name to the Alert')
def step_impl(context):
    try:
        context.application.PracticePage.verify_alert()
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"  

@when(u'Get and show the courses at this price')
def step_impl(context):
    try:
        context.application.PracticePage.get_courses_for_price()
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"          


@when(u'Get me all the people with the position')
def step_impl(context):
    try:
        context.application.PracticePage.get_names_for_position()
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"       

@when(u'Get text from iFrame')
def step_impl(context):
    try:
        context.application.PracticePage.getTextInsideiFrame()
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"             



















@when(u'Pulsar boton continuar en la pagina de bienvenida')
def step_impl(context):
    try:
        context.application.PracticePage.ClickOnButtonContinueSetupPage()
    except Exception as ex:
        assert False, f"Fallo el step al hacer click en el boton continuar\n Motivo del Error: {ex}"


@then(u'Mostrar modal de solicitud de permisos de notificacion en la app')
def step_impl(context):
    try:
        context.application.PracticePage.ValidateModalNotificationAndGPS()
    except Exception as ex:
        assert False, f"Fallo el step al validar modal de acceso a notificaciones y GPS\n Motivo del Error: {ex}"


@when(u'Pulsar boton continuar de la modal de permisos de notificacion y ubicacion')
def step_impl(context):
    try:
        context.application.PracticePage.ClickOnButtonContinueOfModal()
    except Exception as ex:
        assert False, f"Fallo el step al hacer click en continuar dentro de la modal de acceso\n Motivo del Error: {ex}"


@then(u'Mostrar modal de permisos para permitir acceso a ubicacion del dispositivo')
def step_impl(context):
    try:
        context.application.PracticePage.ValidateAlertOfPermission()
    except Exception as ex:
        assert False, f"Fallo el step al validar que se muestre la modal de permisos\n Motivo del Error: {ex}"


@when(u'Pulsar boton "Mientras la app esta en uso"')
def step_impl(context):
    try:
        context.application.PracticePage.ClickOnButtonAccepPermission()
    except Exception as ex:
        assert False, f"Fallo el step al hacer click en conceder permisos de GPS\n Motivo del Error: {ex}"


@then(u'Validar que redireccione a la pagina Initial steps')
def step_impl(context):
    try:
        context.application.PracticePage.ValidatePageLoginInitialSteps()
    except Exception as ex:
        assert False, f"Fallo el step al validar la visualizacion de login page\n Motivo del Error: {ex}"
