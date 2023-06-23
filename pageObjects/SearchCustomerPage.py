
class SearchCustomer:

    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFirstName_xpath = "//input[@id='SearchFirstName']"
    txtLastName_xpath = "//input[@id='SearchLastName']"
    btnSearch_xpath = "//button[@id='search-customers']"

    tableSearchResults_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element("xpath",self.txtEmail_xpath).clear()
        self.driver.find_element("xpath",self.txtEmail_xpath).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element("xpath",self.txtFirstName_xpath).clear()
        self.driver.find_element("xpath", self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element("xpath",self.txtLastName_xpath).clear()
        self.driver.find_element("xpath", self.txtLastName_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element("xpath",self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements("xpath",self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements("xpath",self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element("xpath",self.table_xpath)
            emailid = table.find_element("xpath","//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element("xpath", self.table_xpath)
            name = table.find_element("xpath", "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag