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