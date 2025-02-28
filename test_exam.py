import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from reusable import do_scroll
from pageoject import *
import re


 
 
@pytest.mark.usefixtures("launch_app")
class TestSwaglabs:
    # login in to the swagslab
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

    def test_validate_low_to_high(self):
        try:
            el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=grid_button())
            el1.click()
            time.sleep(3)
            el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=filter_button)
            el2.click()
            time.sleep(3)
            el3 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=low_to_high())
            el3.click()
            time.sleep(3)
            first_item_price = self.driver.find_element(AppiumBy.XPATH,low_price1()).text
            match = re.search(r'\d+\.\d+', first_item_price)
            if match:
                entire_value1 = float(match.group())
                print(f"first product price: {entire_value1}")  

            second_item_price = self.driver.find_element(AppiumBy.XPATH,low_price2()).text
            match2 = re.search(r'\d+\.\d+', second_item_price)
            if match2:
                entire_value2 = float(match.group())
                print(f"Second product price: {entire_value2}")  
            if (entire_value1 < entire_value2):
                print("first product price is less than second product")
        except:
            print("validating price from low to high is failed") 

    def test_validate_high_to_low(self):
        try:
            el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=filter_button())
            el1.click()
            time.sleep(3)
            el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=high_to_low())
            el2.click()
            time.sleep(3)
            first_item_price = self.driver.find_element(AppiumBy.XPATH,high_price1()).text
            match = re.search(r'\d+\.\d+', first_item_price)
            if match:
                entire_value1 = float(match.group())
                print(f"first product price: {entire_value1}")  

            second_item_price = self.driver.find_element(AppiumBy.XPATH,high_price2()).text
            match2 = re.search(r'\d+\.\d+', second_item_price)
            if match2:
                entire_value2 = float(match.group())
                print(f"Second product price: {entire_value2}")  
            if (entire_value1 > entire_value2):
                print("first product price is higher than than second product")
              

        except:
            print("validating price from high to low is failed")            
    
    def test_product_details(self):
        try:
            product_count = len(self.driver.find_elements(AppiumBy.XPATH, product_count()))
            print("product count == ",product_count)

            for i in range(1,product_count+1):
                product_name = self.driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@content-desc='test-Item title'])[" + i + "]").text
                print(product_name)  

        except:
            print("validating price from high to low is failed")   


    def test_checkout(self):
        try:
            el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=add_product())
            el1.click()
            time.sleep(3)

            el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=add_product())
            el2.click()
            time.sleep(3)

            self.driver.find_element(AppiumBy.XPATH,nav_to_cart()).click()
            time.sleep(3)

            do_scroll(self.driver)
            time.sleep(3)

            self.driver.find_element(AppiumBy.XPATH,checkout()).click()
            time.sleep(3)

            el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=checkout_firstname())
            el1.send_keys("salman")
            time.sleep(3)
            el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=checkout_lastname())
            el2.send_keys("shamsudheen")
            time.sleep(3)
            el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=checkout_postal())
            el3.send_keys("66675")
            time.sleep(3)
            el4 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=finish_continue())
            el4.click()  
            time.sleep(3) 


            do_scroll(self.driver)
            
            time.sleep(3)

            self.driver.find_element(AppiumBy.XPATH,finish_button()).click()
            time.sleep(3)
            
            self.driver.find_element(AppiumBy.XPATH,back_to_home()).click()
            time.sleep(3)

        except:
            print("validating price from high to low is failed")
        

         