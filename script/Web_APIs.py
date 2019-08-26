from selenium import webdriver
from selenium.webdriver.support.ui import Select # For dropdown_set()
from selenium.webdriver.common.action_chains import ActionChains # For move_cursor_onto()

from selenium.webdriver.common.by import By # For WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait # For WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # For WebDriverWait

import time
###### Done features ####
# settings              : Import Settings 
# open                  : Open a browser 
# close                 : Close a browser 
# refresh               : Refresh(F5) a browser 
# locate                : Find the locate element , current only supports XPATH 
# locate_frame          : Find the locate element of the Frame
# label_get             : Get a Label string 
# textbox_set           : Input to a textbox 
# textbox_get           : Get the content of a textbox 
# textbox_clear         : Clear a textbox 
# click_button          : Click a button 
# get_button_state      : Get a button's state
# dropdown_set          : Set a dropdown menu
# dropdown_get          : Get a dropdown menu 
# checkbox_click        : Click a checkbox 
# checkbox_get          : Get a checkbox's state 
# switch_window         : Switch a window 
# close_window          : Close a selected window 
# get_window_title      : Get a selected window's title 
# move_cursor_onto      : Move mouse cursor onto a selected location 
# get_single_attribute  : Get the single attribute 
# get_alert_message     : Get a alert window's message 
# accept_alert_message  : To accept a alert window 
# dismiss_alert_message : To dismiss a alert window 
# input_alert_message   : Input some words to a alert window 
# wait_loading_state    : 
# get_css_property      : Get the selected element's css property 

###### Future features ########### 
# radiobutton_set                :
# radiobutton_get                : 
# dialog                         : 
# get_expand_accordion_tab_state : 


class WebConnection():

    driver = webdriver.Chrome("drivers\chromedriver.exe")
   
    def settings(self, type , ip , username , password , port):

        self.type = type
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.get_url = type + "://" + ip + ":" + port

    # driver.get(url)
    def open(self):
        try:
            self.driver.get(self.get_url)
        except Exception as error:
            print(error)

    # driver.quit()
    def close(self):
        try:
            self.driver.quit()
        except Exception as error:
            print(error)
            
    # driver.refresh()
    def refresh(self):
        try:
            self.driver.refresh()
        except Exception as error:
            print(error)
            
    # driver.find_element_by_xpath(xpath)
    def locate(self,xpath):
        try:
            self.wait_loading_state()
            if self.loading_state:
                self.inputElement = self.driver.find_element_by_xpath(xpath) #Without wait time
            # if isButton:
            #     self.inputElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            # else:
            #     self.inputElement = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            #return self.inputElement
        except Exception as error:
            print("###### Error occurs ######")
            print(error)

    # Frame_locate = driver.find_element_by_xpath(frame_xpath)
	# Frame_inputElement = driver.switch_to.frame(Frame_locate)
    def locate_frame(self,frame_xpath):
        try:
            self.frame_locate = self.driver.find_element_by_xpath(frame_xpath)
            self.frame_inputElement = self.driver.switch_to.frame(self.frame_locate)
			#return self.frame_inputElement
        except Exception as error:
            print(error)
			
    # driver.find_element_by_xpath(xpath).text
    def label_get(self):
        try:
            self.value =self.inputElement.text
            return self.value
        except Exception as error:
            print(error)

    # driver.find_element_by_xpath(xpath).send_keys(value)
    def textbox_set(self,value):
        try:
            self.inputElement.send_keys(value)
        except Exception as error:
            print(error)

    # driver.find_element_by_xpath(xpath).get_attribute('value')
    def textbox_get(self):
        try:
            return self.inputElement.get_attribute('value')
        except Exception as error:
            print(error)

    # driver.find_element_by_xpath(xpath).clear()
    def textbox_clear(self):
        try:
            self.inputElement.clear()
        except Exception as error:
            print(error)
            
    # driver.find_element_by_xpath(xpath).click()
    def click_button(self):
        try:
            self.inputElement.click()
        except Exception as error:
            print(error)

    # driver.find_element_by_xpath(xpath).is_enabled()
    def get_button_state(self):
        try:
            return self.inputElement.is_enabled()
        except Exception as error:
            print(error)

    # select = Select(driver.find_element_by_xpath(xpath))
    # select.select_by_index(index)
    def dropdown_set(self,dropdown_select_value):
        self.dropdown_select_value = dropdown_select_value
        try:
            self.select = Select(self.inputElement)
            self.select.select_by_index(self.dropdown_select_value)
        except Exception as error:
            print(error)

    # driver.find_element_by_xpath(xpath).get_attribute('value')
    def dropdown_get(self):
        try:
            return self.inputElement.get_attribute('value')
        except Exception as error:
            print(error)
    # driver.find_element_by_xpath(xpath).click()
    def checkbox_click(self):
        try:
            self.inputElement.click()
        except Exception as error:
            print(error)

    # driver.find_element_by_xpath(xpath).is_selected()
    def checkbox_get(self):
        try:
            return self.inputElement.is_selected()
        except Exception as error:
            print(error)

    # windows = driver.window_handles
    # driver.switch_to.window(windows[Window_Count])
    def switch_window(self , Window_Count):    
        self.Window_Count = Window_Count
        self.windows = self.driver.window_handles
        delays(3)
        self.driver.switch_to.window(self.windows[self.Window_Count])

    # windows = driver.window_handles
    # driver.switch_to.window(windows[Window_Count])   
    # driver.close()    
    def close_window(self , Window_Count):
        self.Window_Count = Window_Count
        self.windows = self.driver.window_handles
        delays(3)
        self.driver.switch_to.window(self.windows[self.Window_Count])
        self.driver.close()

    # windows = driver.window_handles
    # driver.switch_to.window(windows[Window_Count])   
    # driver.title   
    def get_window_title(self , Window_Count):
        self.Window_Count = Window_Count
        self.windows = self.driver.window_handles
        delays(3)
        self.driver.switch_to.window(self.windows[self.Window_Count])
        Title = self.driver.title
        return Title

    # hover = ActionChains(driver).move_to_element(inputElement)
    # hover.perform()    
    def move_cursor_onto(self):
        self.hover = ActionChains(self.driver).move_to_element(self.inputElement)
        self.hover.perform()    
    
    
    def get_single_attribute(self , attribute):
        try:
            return self.inputElement.get_attribute(attribute)
        except Exception as error:
            print(error)
            
    # Alert has no xpath 
	# a1 = driver.switch_to.alert
	# return a1.text
    def get_alert_message(self):   
        try:
            self.a1 = self.driver.switch_to.alert
            delays(1)
            return self.a1.text
        except Exception as error:
            print(error)

    # a1.accept() => accept the alert 
    def accept_alert_message(self):   
        try:
            self.a1.accept()
        except Exception as error:
            print(error)

    # a1.dismiss() => dismiss the alert , cancel
    def dismiss_alert_message(self):   
        try:
            self.a1.dismiss()
        except Exception as error:
            print(error)

    # a1.send_keys(alert_input) => send some words into the alert window
    def input_alert_message(self , alert_input):   
        try:
            self.a1.send_keys(alert_input)
            delays(1)
            self.a1.accept()
        except Exception as error:
            print(error)

    # For Blueplate project , wait the loading icon disappears
    def wait_loading_state(self):
        try:
            self.wait = WebDriverWait(self.driver,10)
            self.loading_state = self.wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
            delays(1)
            print(self.loading_state)
        except Exception as error:
            print(error)    
    
    # Refer to https://www.w3schools.com/cssref/ to select the css property
    def get_css_property(self,property_name):
        try:
            return self.inputElement.value_of_css_property(property_name)
        except Exception as error:
            print(error)
    
def delays(seconds, reason = ""):
    if seconds > 3:
        if reason == "":
            print("Waiting for %d seconds..." %seconds)
        else:
            print("Waiting for %d seconds due to %s..." %(seconds, reason))

        current = seconds
        while current > 0:
            time.sleep(1)
            current -= 1
            second_str = "%d seconds...\r" %current
            print(second_str, end='')
        print("")
    else:
        time.sleep(seconds)