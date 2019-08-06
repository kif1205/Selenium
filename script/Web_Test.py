from Web_APIs import *

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
Web_IP = "10.162.246.133"
Web_Account = "admin"
Web_Password = "Password1"
Web_Port = "8080"

def Web_Open():

    global Web_Test

    Web_Test = WebConnection()
    Web_Test.settings(Web_Connect_Type , Web_IP, Web_Account , Web_Password ,Web_Port)
    Web_Test.open()
	
def Web_Close():
    Web_Test.close()

def main():

    Web_Open()

    # Input Account Name
    Web_Test.locate("/html/body/app-root/div/div/div/app-login/div/div/div/div/form/div[2]/input[1]")
    Web_Test.textbox_set("admin")
    
    # Input Account Password
    Web_Test.locate("/html/body/app-root/div/div/div/app-login/div/div/div/div/form/div[2]/input[2]")
    Web_Test.textbox_set("Password1")
    #delays(3)
    
    # Click Login Button
    Web_Test.locate("/html/body/app-root/div/div/div/app-login/div/div/div/div/form/button")
    Web_Test.click_button()
    #delays(5)
    
    # #######################
    # # Change KVM Settings #
    # #######################
    # # Switch to Virtual Console tab
    # Web_Test.locate("/html/body/app-root/div/div/div[1]/app-sidenav/div/ul/li[8]/a")
    # Web_Test.click_button()
    # delays(3)
    # 
    # # Clear KVM Port textbox
    # Web_Test.locate("/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[2]/app-vconsole/div/div[2]/form/div[3]/div/input")
    # Web_Test.textbox_clear()
    # 
    # Web_Test.textbox_set("1111")
    # 
    # 
    # # Get KVM Port
    # Web_Test.locate("/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[2]/app-vconsole/div/div[2]/form/div[3]/div/input")
    # kvmport = Web_Test.textbox_get()
    # print(kvmport)
    
    #
    # # Get KVM Port label
    # Web_Test.locate("/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[2]/app-vconsole/div/div[2]/form/div[3]/label")
    # kvmport_label = Web_Test.label_get()
    # print(kvmport_label)
    #
    # # Get KVM Viewer button state
    # Web_Test.locate("/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[2]/app-vconsole/div/div[1]/div/div[2]/div/button[1]")
    # kvm_viewer_button_state = Web_Test.get_button_state()
    # print(kvm_viewer_button_state)

    # # Change Boot Source Target
    # Web_Test.locate("/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[1]/app-boot/div/div[2]/div/div[2]/div[2]/select")
    # Web_Test.dropdown_set(1)
    # delays(3)
    # Web_Test.dropdown_set(2)
    # 
    # # Get Boot Source Target
    # Web_Test.locate("/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[1]/app-boot/div/div[2]/div/div[2]/div[2]/select")
    # bootsource = Web_Test.dropdown_get()
    # print(bootsource)


    # # Click KVM Enabled checkbox
    # Web_Test.locate("//app-remotecontrol//app-vconsole//div[2]/form/div[1]//input")
    # #Web_Test.locate("//input[@formcontrolname='kvmEnabled']")
    # Web_Test.checkbox_click()
    # 
    # #Web_Test.locate("/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[2]/app-vconsole/div/div[2]/form/div[1]/div/input")
    # checkbox_state =  Web_Test.checkbox_get()  
    # print(checkbox_state)  
    
    
    # # Open KVM Viewer 
    # Web_Test.locate("/html/body/app-root/div/div/div[2]/app-remotecontrol/div/div[2]/div/div[2]/app-vconsole/div/div[1]/div/div[2]/div/button[1]")
    # Web_Test.click_button()
    # delays(5)
    # 
    # # Switch to KVM Viewer and get the title
    # Web_Test.switch_window(1) 
    # window_1_title = Web_Test.get_window_title(1)
    # print(window_1_title)
    # 
    # # Get the current Available VM Menu
    # Web_Test.locate('//*[@id="navbarDropdownMenuVMedia"]')
    # Web_Test.click_button()
    # delays(3)
    # 
    # Web_Test.locate('//*[@id="navbarSupportedContent"]/ul/li[5]/div')
    # VM_Menu = Web_Test.get_single_attribute("outerText")
    # delays(1)
    # 
    # VM_Menu = VM_Menu.split("\n")
    # print(VM_Menu)
    # 
    # # Close KVM Viewer
    # Web_Test.close_window(1) 
    # 
    # # Switch to Main Window and get the title
    # Web_Test.switch_window(0)
    # window_0_title = Web_Test.get_window_title(0)
    # print(window_0_title)
    


    # ########################
    # # Change BIOS Settings #
    # ########################
    # # Switch to BIOS Settings tab
    # Web_Test.locate("/html/body/app-root/div/div/div[1]/app-sidenav/div/ul/li[9]/a")
    # Web_Test.click_button()
    # delays(3)
    # 
    # Web_Test.locate('//*[@id="navbarDropdownMenuFile"]')
    # Web_Test.click_button()
    # delays(2)
    # 
    # Web_Test.locate('//*[@id="navbarSupportedContent"]/ul/li/div/div[3]/div/ul/li/a')    
    # Web_Test.move_cursor_onto()
    # delays(1)
    # 
    # Web_Test.locate('//*[@id="navbarSupportedContent"]/ul/li/div/div[3]/div/ul/li/div/ul/li/a') 
    # Web_Test.click_button()
    # delays(1)
    
    # ###############
    # # Dialog Test #
    # ###############
    # # Test Delete SEL Logs
    # # Switch to Logs Settings tab
    # Web_Test.locate("/html/body/app-root/div/div/div[1]/app-sidenav/div/ul/li[3]/a")
    # Web_Test.click_button()
    # delays(3)
    # 
    # # Click the Delete SEL Button
    # Web_Test.locate('/html/body/app-root/div/div/div[2]/app-logs/div/div[2]/div/div/div/app-eventlog/div/div/div/div[1]/div[2]/div[1]/a/i')
    # Web_Test.click_button()
    # delays(3)
    #     
    # Web_Test.locate("/html/body/app-root/div/div/div[2]/app-message-dialog/app-message-modal/div/div/div/div[2]/div/div/div")
    # test_dialog_1 = Web_Test.label_get()
    # print(test_dialog_1)
    # 
    # Web_Test.locate("/html/body/app-root/div/div/div[2]/app-message-dialog/app-message-modal/div/div/div/div[3]/div/button[2]")
    # Web_Test.click_button()
    # delays(3)    
    # 
    # Web_Test.locate('//*[@id="extendedInfoDialog"]/div/div[2]/div/div/div/div')
    # test_dialog_2 = Web_Test.label_get()
    # print(test_dialog_2)
    # delays(3)     
    # 
    # Web_Test.locate('//*[@id="extendedInfoDialog"]/div/div[3]/div/button')
    # Web_Test.click_button()
    # delays(3)     
    
    ##############################
    # Firmware Update management #
    ##############################
    # Switch to Firmware tab
    Web_Test.locate("//app-sidenav/div/ul/li[7]/a")
    Web_Test.click_button()
    #delays(3)
    
    Web_Test.locate("//input[@name='txtTFTPPath']")
    Web_Test.textbox_clear()
    #delays(3)
    
    Web_Test.locate("//input[@name='txtTFTPPath']")
    Web_Test.textbox_set("tftp://1.1.1.1")
    #delays(3)
    
    Web_Test.locate("//div[@class='accordion-group']//fieldset[@class='scheduler-border']//button[@class='btn btn-vertiv']")
    Web_Test.click_button()
    #delays(3)    
    # 
    Web_Test.locate("//div[contains(@class, 'accordion-group')]//fieldset[contains(@class,'scheduler-border')]//div[contains(@class,'col-md-6')]//div[contains(@class,'font-italic font-weight-bold')]")
    test = Web_Test.label_get()
    # #delays(3)  
    print(test)
    # 
    #Web_Test.refresh()
    #Web_Close()
if __name__ == "__main__":
    main()
