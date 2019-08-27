from Web_APIs import *
from selenium.webdriver.common.keys import Keys
import csv

# The ways to copy path 
# 1. Copy outer HTML => <input formcontrolname="kvmEnabled" name="chkKVM" type="checkbox" class="ng-valid ng-dirty ng-touched">
#    XPath can be "//input[@formcontrolname='kvmEnabled']"
# 2. Copy Xpath => "/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[2]/app-vconsole/div/div[2]/form/div[1]/div/input"
#    XPath can be //app-remotecontrol//app-vconsole//div[2]/form/div[1]//input
#
# 3. XPath examples :  //div[contains(@class, 'accordion-group')] => div is the function name before class like this "<div class="pt-2">" => function name is "div"
#                      <input disabled="" type="radio" id="rdoUploadType2bmc" class="ng-untouched ng-pristine"> => function name is "input"
#    XPath_TFTP_Button = "//*[contains(@class, 'accordion-group')]//*[contains(@class,'form ng-valid ng-dirty ng-touched')]//*[contains(@class,'scheduler-border')]//*[contains(@class,'btn btn-vertiv')]"
#    XPath_TFTP_Button = "//app-accordion//app-firmware-inventory/form/div/div[4]/fieldset/div/div/div[2]/button"
     
#    XPath_TFTP_Button = "//div[contains(@class, 'accordion-group')]//fieldset[contains(@class,'scheduler-border')]//button[contains(@class,'btn btn-vertiv')]"
#    XPath_TFTP_Button = "//div[@class='accordion-group']//fieldset[@class='scheduler-border']//button[@class='btn btn-vertiv']"
    
Web_Type = "Chrome"
Web_Connect_Type = "https"
Web_IP = "mops.twse.com.tw/mops/web/stapap1"
Web_Port = ""
Web_Account = ""
Web_Password = ""

def Web_Open():

    global Web_Test

    Web_Test = WebConnection()
    Web_Test.settings(Web_Connect_Type , Web_IP, Web_Account , Web_Password , Web_Port)
    Web_Test.open()
	
def Web_Close():
    Web_Test.close()
    
def main():

    Web_Open()
    
    Web_Test.locate('//*[@id="co_id"]')
    Web_Test.textbox_set("2330")
    delays(1)
    
    Web_Test.locate('//*[@id="PageBody"]/table/tbody/tr/td[3]')
    Web_Test.click_button()
    delays(1)
    
    Web_Test.locate('//input[@value=" 查詢 "]')
    Web_Test.click_button()
    delays(3)

    Web_Test.locate('//table[@class="hasBorder"]')
    table = Web_Test.get_table()
    
    for item in table:
        print(item)

    with open("2330.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        
        for item in table:
            wr.writerow(item)
    
    #Web_Test.refresh()
    
    
    #Web_Close()
    
if __name__ == "__main__":
    main()
