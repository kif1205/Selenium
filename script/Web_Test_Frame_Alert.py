from Web_APIs import *

# The ways to copy path 
# 1. Copy outer HTML => <input formcontrolname="kvmEnabled" name="chkKVM" type="checkbox" class="ng-valid ng-dirty ng-touched">
#    XPath can be "//input[@formcontrolname='kvmEnabled']"
# 2. Copy Xpath => "/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[2]/app-vconsole/div/div[2]/form/div[1]/div/input"
#    XPath can be //app-remotecontrol//app-vconsole//div[2]/form/div[1]//input

Web_Type = "Chrome"
Web_Connect_Type = "http"
Web_IP = "nt.kfsh.hc.edu.tw"
Web_Account = "admin"
Web_Password = "Password1"
Web_Port = "80"


def Web_Open():

    global Web_Test

    Web_Test = WebConnection()
    Web_Test.settings(Web_Connect_Type , Web_IP, Web_Account , Web_Password ,Web_Port)
    Web_Test.open()
	
def Web_Close():
    Web_Test.close()

def main():

    Web_Open()

    Web_Test.locate_frame('//*[@id="loginPage"]')
    Web_Test.locate("//input[@name='txtAccount']")
    Web_Test.textbox_set("admin")

    Web_Test.locate("//input[@name='txtPassword']")
    Web_Test.textbox_set("admin")

    Web_Test.locate('/html/body/main/form/div[2]/div[2]/div[2]/button')
    Web_Test.click_button()
    delays(1)
	
    test1 = Web_Test.get_alert_message()
    print(test1)
    delays(1)
    Web_Test.accept_alert_message()
    
    test2 = Web_Test.get_alert_message()
    print(test2)
    delays(1)
    Web_Test.accept_alert_message()
    
    #Web_Test.refresh()
    #Web_Close()
if __name__ == "__main__":
    main()

