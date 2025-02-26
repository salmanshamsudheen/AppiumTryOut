from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
 
class Quest:
    cap = {
        "deviceName" : "Samsung",
        "platformName" : "Android",
        "automationName" : "UiAutomator2",
       # "version" : "9.0",
       # "udid" : "emulator-5554",
        "browserName" : "chrome",
        "chromedriverExecutable" : "D:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    }

    def initiate_Driver(self):
 
    #self.appium_service =AppiumService()
    #global appium service
        try:
            global driver
            #driver = webdriver.Remote("http:localhost:4723/wd/hub", self.desired_caps)
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
        except TypeError:
            print("error: Appium Server is not Working ....")
            self.appium_Service.stop()
   
    def launch_Appium_Driver(self):
   
        driver.get("https://www.quest-global.com/")
        time.sleep(15)

    def test1(self):
        try:
            driver.find_element(AppiumBy.XPATH, "//*[@id='navbar_top']/div/button/span").click()
            time.sleep(5)

            count = len(driver.find_elements(AppiumBy.XPATH, '//*[@id="nav_mobile"]/ul/li'))

            for i in range(1,count+1):
                item = driver.find_element(AppiumBy.XPATH, "(//*[@id='nav_mobile']/ul/li/a)[" +str(i)+ "]").text
                print(item)
        except:
            print("Test failed") 


    def quit_session(self):
        driver.quit()           

obj = Quest()
obj.initiate_Driver()
obj.launch_Appium_Driver()
obj.test1()
obj.quit_session()
