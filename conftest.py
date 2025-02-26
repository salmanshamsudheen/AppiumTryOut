import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
 
@pytest.fixture(scope="function")
def launch_app(request):
    try:
        cap = {
        "deviceNAme": "Samsung",
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "app": "c:\\Users\\"
    }
        print("Initiating app instance driver")
        driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
        request.instance.driver = driver
 
        yield driver
 
        driver.quit()
    except:
        print("Unable to launch the app")
