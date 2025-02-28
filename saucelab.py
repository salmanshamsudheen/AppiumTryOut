from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
from reusable import do_scroll
import re

 
 
 
class Swaglabs:
 
   
    cap = {
            "appium:deviceName": "Samusung",
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:app": "C:\\Users\\2022403\\Downloads\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
            "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity"
            }
 
    def initiate_Driver(self):
        #self.apppium_service = AppiumService()
        #global appium_service
       
        try:
            global driver
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout": 500})
        except TypeError:
            print("Error:Appium server not working ...")
 
    def launch_app(self):
        try:
            driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Username']").send_keys("standard_user")
            time.sleep(4)
            driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Password']").send_keys("secret_sauce")
            time.sleep(4)
            driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-LOGIN']").click()
            time.sleep(4)


            el1 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(4)")
            el1.click()
            time.sleep(3)
            el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(5)")
            el2.click()
            time.sleep(3)
            el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Price (low to high)\")")
            el3.click()
            time.sleep(3)
            first_item_price = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="test-Price" and @text="$7.99"]').text
            match = re.search(r'\d+\.\d+', first_item_price)
            if match:
                entire_value1 = float(match.group())
                print(f"first product price: {entire_value1}")  

            second_item_price = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="test-Price" and @text="$9.99"]').text
            match2 = re.search(r'\d+\.\d+', second_item_price)
            if match2:
                entire_value2 = float(match.group())
                print(f"Second product price: {entire_value2}")  
            if (entire_value1 < entire_value2):
                print("first product price is less than second product")

            product_count = len(driver.find_elements(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-Item']"))
            print("product count == ",product_count)
            for i in range(1,product_count+1):
                product_name = driver.find_element(AppiumBy.XPATH,"(//android.view.ViewGroup[@content-desc='test-Item'])[" + i + "]/android.widget.TextView").text
                print(product_name)     
        except:
            print("there is an issue in Login")
 
    # def add_cart(self):
    #     try:
    #         driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@text='ADD TO CART'])[1]").click()
    #         time.sleep(4)
    #         driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='ADD TO CART']").click()
    #         time.sleep(4)

    #     except:
    #         print("add to cart issue")
    
    # def validate_add_cart(self):

    # #    count = len(driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='REMOVE']"))
    # #    print("The no of cart items is,",count)
    
	
    #    if driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='2']").is_displayed :
    #        print("this is 2 cat added")
             
    # def checkout(self):
    #     driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.view.ViewGroup").click()
    #     time.sleep(4)

    #     do_scroll(driver)
    #     time.sleep(4)

    #     driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-CHECKOUT']").click()
    #     time.sleep(4)

    #     el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-First Name")
    #     el1.send_keys("salman")
    #     time.sleep(4)
    #     el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Last Name")
    #     el2.send_keys("shamsudheen")
    #     time.sleep(4)
    #     el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Zip/Postal Code")
    #     el3.send_keys("66675")
    #     time.sleep(4)
    #     el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"CONTINUE\")")
    #     el4.click()  
    #     time.sleep(4) 


    #     do_scroll(driver)

        
    #     time.sleep(4)

    #     driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-FINISH']").click()
    #     time.sleep(4)
        
    

    #     driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='BACK HOME']").click()
    #     time.sleep(4)
        

    def quit_session(self):
        driver.quit()
 
obj=Swaglabs()
obj.initiate_Driver()
obj.launch_app()
# obj.add_cart()
# obj.validate_add_cart()
# obj.checkout()
obj.quit_session()
 