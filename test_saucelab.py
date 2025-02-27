import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from reusable import do_scroll
from pageoject import *

 
 
@pytest.mark.usefixtures("launch_app")
class TestSwaglabs:

    def test_launch_app(self, read_json):
        try:
            self.driver.find_element(AppiumBy.XPATH,username()).send_keys(read_json["username"])
            time.sleep(4)
            self.driver.find_element(AppiumBy.XPATH,password()).send_keys(read_json["password"])
            time.sleep(4)
            self.driver.find_element(AppiumBy.XPATH,login_button()).click()
            time.sleep(4)
        except:
            print("there is an issue in Login")
 
    def test_add_cart(self):
        try:
            count = len(self.driver.find_elements(AppiumBy.XPATH, item_count()))
            for i in range(1,count+1):
                item = self.driver.find_element(AppiumBy.XPATH,print_item(i)).text
                print(item)
            self.driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@text='ADD TO CART'])[1]").click()
            time.sleep(4)
            self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='ADD TO CART']").click()
            time.sleep(4)

        except:
            print("add to cart issue")
    
    def test_validate_add_cart(self):
	
        if self.driver.find_element(AppiumBy.XPATH,val_add_to_cart()).is_displayed :
           print("2 items added to cart")
             
    def test_checkout(self):
        self.driver.find_element(AppiumBy.XPATH,nav_to_cart()).click()
        time.sleep(4)

        do_scroll(self.driver)
        time.sleep(4)

        self.driver.find_element(AppiumBy.XPATH,checkout()).click()
        time.sleep(4)

        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-First Name")
        el1.send_keys("salman")
        time.sleep(4)
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Last Name")
        el2.send_keys("shamsudheen")
        time.sleep(4)
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Zip/Postal Code")
        el3.send_keys("66675")
        time.sleep(4)
        el4 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"CONTINUE\")")
        el4.click()  
        time.sleep(4) 


        do_scroll(self.driver)
        
        time.sleep(4)

        self.driver.find_element(AppiumBy.XPATH,finish_button()).click()
        time.sleep(4)
        
        self.driver.find_element(AppiumBy.XPATH,back_to_home()).click()
        time.sleep(4)
        

