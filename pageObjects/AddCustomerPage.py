import time

from selenium.webdriver.support.ui import Select

class AddCustomer:
    lnkCustomer_menu_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btnAddnew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtNewsLetter_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
    litemYourStore_xpath = "//li[contains(text(),'Your store name')]"
    litemTestStore_xpath = "//li[contains(text(),'Test store 2')]"
    txtcustomerRoles_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    listitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    listitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    listitemGuests_xpath = "//li[contains(text(),'Guests')]"
    listitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element("xpath",self.lnkCustomer_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element("xpath",self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element("xpath",self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element("xpath",self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element("xpath",self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element("xpath",self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element("xpath",self.txtLastName_xpath).send_keys(lname)

    def setDOB(self, dob):
        self.driver.find_element("xpath",self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element("xpath",self.txtCompanyName_xpath).send_keys(comname)

    def setNewsLetter(self,news):
        self.driver.find_element("xpath",self.txtNewsLetter_xpath).click()
        time.sleep(3)
        if news == 'Your store name':
            self.litem = self.driver.find_element("xpath",self.litemYourStore_xpath)
        else:
            self.litem = self.driver.find_element("xpath",self.litemTestStore_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click;", self.litem)

    def setCustomerRoles(self,role):
        self.driver.find_element("xpath",self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element("xpath",self.listitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element("xpath",self.listitemAdministrators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element("xpath","//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[2]").click()
            self.listitem = self.driver.find_element("xpath",self.listitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element("xpath",self.listitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element("xpath",self.listitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element("xpath",self.listitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click;",self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element("xpath",self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element("xpath",self.rdMaleGender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element("xpath",self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element("xpath",self.rdMaleGender_xpath).click()

    def setAdminComment(self, comment):
        self.driver.find_element("xpath",self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element("xpath",self.btnSave_xpath).click()


