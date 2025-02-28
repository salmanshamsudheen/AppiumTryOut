def username():
    return "//android.widget.EditText[@content-desc='test-Username']"

def password():
    return "//android.widget.EditText[@content-desc='test-Password']"

def login_button():
    return "//android.view.ViewGroup[@content-desc='test-LOGIN']"

def item_count():
    return "//android.widget.TextView[@content-desc='test-Item title']"
 
def print_item(i):
    return "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]"

def val_add_to_cart():
    return "//android.widget.TextView[@text='2']"

def nav_to_cart():
    return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.view.ViewGroup"

def checkout():
    return "//android.view.ViewGroup[@content-desc='test-CHECKOUT']"
 
def finish_button():
    return "//android.view.ViewGroup[@content-desc='test-FINISH']"

def back_to_home():
    return "//android.widget.TextView[@text='BACK HOME']"

def grid_button():
    return "new UiSelector().className(\"android.widget.ImageView\").instance(4)"

def filter_button():
    return "new UiSelector().className(\"android.widget.ImageView\").instance(5)"

def low_to_high():
    return "new UiSelector().text(\"Price (low to high)\")"

def low_price1():
    return '//android.widget.TextView[@content-desc="test-Price" and @text="$7.99"]'

def low_price2():
    return '//android.widget.TextView[@content-desc="test-Price" and @text="$9.99"]'

def high_to_low():
    return "new UiSelector().text(\"Price (high to low)\")"

def high_price1():
    return '//android.widget.TextView[@content-desc="test-Price" and @text="$49.99"]'

def high_price2():
    return '//android.widget.TextView[@content-desc="test-Price" and @text="$29.99"]'

def product_count():
    return "//android.view.ViewGroup[@content-desc='test-Item']"

def checkout_firstname():
    return "test-First Name"

def checkout_lastname():
    return "test-Last Name"

def checkout_postal():
    return "test-Zip/Postal Code"

def finish_continue():
    return "new UiSelector().text(\"CONTINUE\")"

def add_product():
    return "new UiSelector().text(\"+\").instance(0)"