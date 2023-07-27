import time
import warnings

import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from app.application import Application
from configuration.config import Datatest


def before_scenario(context, scenario):
    print("################")
    print("[ CONFIGURACION ] - Inicializando la configuracion del controlador")
    print("################")
    caps = None
    if Datatest.OS.upper() == "ANDROID":
        caps = Datatest.ANDROID_CONFIG
        caps["appium:headless"] = True
    else:
        caps = Datatest.IOS_CONFIG
    if caps is None:
        assert False, f"Error no hay data en los capabilities, el valor es: {caps}"

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        context.driver = webdriver.Remote(Datatest.URL, caps)
        context.driver.implicitly_wait(Datatest.IMPLICIT_WAIT)
        context.application = Application(context.driver)
    print("################")
    print("[ SCENARIO ] - " + scenario.name)
    print("################")


def after_scenario(context, scenario):

    if scenario.status == "failed":
        failed_step_name = None
        scenario_name = scenario.name
        for step in scenario.steps:
            if step.status == "failed":
                failed_step_name = step.name
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
        screenshot_name = f"{scenario_name}_{failed_step_name}_{current_time}.png"
        allure.attach(context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)
        context.driver.close_app()

    print("################")
    print("[  DRIVER STATUS  ] - Limpiando y cerrando instancia del controlador")
    print("################")
    context.driver.quit()

