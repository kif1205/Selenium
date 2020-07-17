from selenium import webdriver
import time
import win32com.client

# Setup
# pip install pypiwin32
# pip install selenium

# Reference :
# Login Window : https://stackoverflow.com/questions/40671662/how-to-handle-windows-authentication-popup-in-selenium-using-pythonplus-java

driver_location = "C:\web_driver\chromedriver.exe"
DUT_location = "http://192.168.1.1"
username = "admin"
password = "22Ejdkhc"

################
# XPath define #
################
Armor_Close              = '//*[@id="armor_close"]'

BASIC_TAB                = '//*[@id="basic_label"]'
ADVANCED_TAB             = '//*[@id="advanced_label"]'

BASIC_Home               = '//*[@id="basic_home"]'
BASIC_Internet           = '//*[@id="basic_internet"]'
BASIC_Wireless           = '//*[@id="basic_wireless"]'
BASIC_Attached_Devices   = '//*[@id="basic_attached"]'
BASIC_Quality_Of_Service = '//*[@id="basic_qos"]'

LOADING_IMG              = "/html/body/div[2]/img"

class my_web:
    None

class dut_web:
    def __init__(self):
        pass

    def open_browser(self , browser_type , driver_location , DUT_location):
        self.driver_location = driver_location
        self.DUT_location = DUT_location

        if browser_type == "chrome":
            self.driver = webdriver.Chrome(self.driver_location)

        self.driver.maximize_window()

    def open_target(self):
        self.driver.get(self.DUT_location)

    def close(self):
        return self.driver.quit()

    # For debug
    def get_driver(self):
        return self.driver

class locator(dut_web):
    def __init__(self):
        pass

    # For debug
    def pri_driver(self):
        print(self.get_driver())

    def locator_by_xpath(self , locator_element):
        try:
            self.inputelement = self.driver.find_element_by_xpath(locator_element)
            return True , self.inputelement
        except:
            return False , None

class label(locator):
    def __init__(self):
        pass

    def label_get(self):
        return self.inputelement.text


class button(locator):
    def __init__(self):
        pass

    def click(self):
        self.inputelement.click()

class frame(locator):
    def __init__(self):
        pass

    def switch_to_sub_frame(self , frame_name):
        self.driver.switch_to.frame(frame_name)

    def switch_to_default_frame(self):
        self.driver.switch_to.default_content()

class attribute(locator):
    def __init__(self):
        pass

    def get_css_property(self , css_property):
        try:
            found_attribute = self.inputelement.value_of_css_property(css_property)
            return True , found_attribute
        except:
            return False , None

    def get_attr(self , attribute_name):
        try:
            found_attribute = self.inputelement.get_attribute(attribute_name)
            return True , found_attribute
        except:
            return False , None




class web_elements(label , button , frame , attribute):
    def __init__(self):
        pass

class web_test(web_elements):
    def __init__(self):
        pass



def DUT_Open(browser_type , driver_location , DUT_location):
    my_web.dut = dut_web()
    my_web.dut.open_browser(browser_type , driver_location , DUT_location)
    my_web.dut.open_target()

def DUT_Login(username , password):
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.Sendkeys(username)
    time.sleep(2)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys(password)
    time.sleep(2)
    shell.Sendkeys("{ENTER}")
    time.sleep(5)

def DUT_Close():
    my_web.dut.close()

# ----------------------------------------------------------------------------------
# Initial
test = web_test()
test.open_browser("chrome" , driver_location , DUT_location)
test.open_target()
DUT_Login(username , password)

test.pri_driver()
#print(test.driver)

# ----------------------------------------------------------------------------------
# Check Armor page if pop up
find_state , inputelement = test.locator_by_xpath(Armor_Close)
print(find_state)
print(inputelement)
if find_state:
    test.click()

time.sleep(5)


'''
# ----------------------------------------------------------------------------------
# Switch BASIC and ADVANCED Tab
find_state , inputelement = test.locator_by_xpath('//*[@id="topframe"]')
print(find_state)
print(inputelement)
if find_state:
    test.switch_to_sub_frame('topframe')

find_state , inputelement = test.locator_by_xpath(BASIC_TAB)
print(find_state)
print(inputelement)
if find_state:
    test.click()

time.sleep(5)

find_state , inputelement = test.locator_by_xpath('//*[@id="topframe"]')
print(find_state)
print(inputelement)
if find_state:
    test.switch_to_sub_frame('topframe')

find_state , inputelement = test.locator_by_xpath(ADVANCED_TAB)
print(find_state)
print(inputelement)
if find_state:
    test.click()

time.sleep(5)

find_state , inputelement = test.locator_by_xpath('//*[@id="topframe"]')
print(find_state)
print(inputelement)
if find_state:
    test.switch_to_sub_frame('topframe')

find_state , inputelement = test.locator_by_xpath(BASIC_TAB)
print(find_state)
print(inputelement)
if find_state:
    test.click()

# Switch to default frame
test.switch_to_default_frame()

time.sleep(5)

# ----------------------------------------------------------------------------------
# Find Router Firmware Version , it needs to switch frame
find_state , inputelement = test.locator_by_xpath('//*[@id="topframe"]')
print(find_state)
print(inputelement)
if find_state:
    test.switch_to_sub_frame('topframe')

find_state , inputelement = test.locator_by_xpath('//*[@id="firm_version"]')
print(find_state)
print(inputelement)
if find_state:
    print(test.label_get())

# Switch to default frame
test.switch_to_default_frame()


# ----------------------------------------------------------------------------------
# Switch to BASIC -> Quality of Service page
find_state , inputelement = test.locator_by_xpath(BASIC_Quality_Of_Service)
print(find_state)
print(inputelement)
if find_state:
    test.click()

# ----------------------------------------------------------------------------------
# Check the display property in CSS property of XPATH://*[@id="formframe_wait_div"] ,
# The property "display" in CSS reveals the current frame page loading state
# Page is loading      => display = block
# Page loaded finished => display = none
find_state , inputelement = test.locator_by_xpath('//*[@id="formframe_wait_div"]')
print(find_state)
print(inputelement)

# display = block , because the frame page is loading
print(test.get_css_property("display"))

time.sleep(20)

# display = none , because the frame page loaded successfully
print(test.get_css_property("display"))


# ----------------------------------------------------------------------------------
# Get the title name of Quality of Service page
find_state , inputelement = test.locator_by_xpath('//*[@id="formframe"]')
print(find_state)
print(inputelement)
if find_state:
    test.switch_to_sub_frame('formframe')

# Read BASIC -> Quality of Service page -> Uplink bandwidth value
find_state , inputelement = test.locator_by_xpath('/html/body/form/div[2]')
print(find_state)
print(inputelement)
if find_state:
    print(test.label_get())
'''

# ----------------------------------------------------------------------------------
# ADVANCED Tab -> Advanced Setup -> Check menu is opened or closed
print("test case : ADVANCED Tab -> Advanced Setup -> Check menu is opened or closed")
find_state , inputelement = test.locator_by_xpath('//*[@id="topframe"]')
print(find_state)
print(inputelement)
if find_state:
    test.switch_to_sub_frame('topframe')

# Switch to ADVANCED TAB
find_state , inputelement = test.locator_by_xpath(ADVANCED_TAB)
print(find_state)
print(inputelement)
if find_state:
    test.click()

time.sleep(5)

# Open ADVANCED Tab -> Advanced Setup
find_state , inputelement = test.locator_by_xpath('//*[@id="advanced_bt"]')
print(find_state)
print(inputelement)
if find_state:
    test.click()

time.sleep(5)

# return_data is "advanced_white_open_button_double" when ADVANCED Tab -> Advanced Setup is opened
find_state , return_data = test.get_attr('class')
print(find_state)
print(return_data)

# Close ADVANCED Tab -> Advanced Setup
if find_state:
    test.click()

time.sleep(5)

# return_data is "advanced_white_close_button_double" when ADVANCED Tab -> Advanced Setup is closed
find_state , return_data = test.get_attr('class')
print(find_state)
print(return_data)

# ----------------------------------------------------------------------------------


#test.close()








