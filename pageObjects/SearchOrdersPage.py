class SearchOrder:
    lnkSales_xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]"
    lnkOrders_xpath = "//p[contains(text(),'Orders')]"
    txtemail_xpath = "//input[@id='BillingEmail']"
    btnSearchOrders_xpath = "//button[@id='search-orders']"

    tabSearchResults_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
    tabResults_xpath = "//table[@id='orders-grid']"
    tabRows_xpath = "//table[@id='orders-grid']//tbody/tr"
    tabColumns_xpath = "//table[@id='orders-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def clickOnSalesMenu(self):
        self.driver.find_element("xpath",self.lnkSales_xpath).click()

    def clickOnOrderMenu(self):
        self.driver.find_element("xpath",self.lnkOrders_xpath).click()

    def setEmail(self,email):
        self.driver.find_element("xpath",self.txtemail_xpath).clear()
        self.driver.find_element("xpath",self.txtemail_xpath).send_keys(email)

    def clickSearch(self):
        self.driver.find_element("xpath",self.btnSearchOrders_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements("xpath",self.tabRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements("xpath",self.tabColumns_xpath))

    def searchOrderByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element("xpath",self.tabResults_xpath)
            emailid = table.find_element("xpath","//table[@id='orders-grid']//tbody/tr["+str(r)+"]/td[6]").text
            if emailid == email:
                flag = True
                break
        return flag