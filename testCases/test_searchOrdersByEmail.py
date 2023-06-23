import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchOrdersPage import SearchOrder

class Test_006_SearchOrder:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_SearchOrders(self,setup):
        self.logger.info("***********Test_003_AddCustomer*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************Login Successful******************")

        self.logger.info("******* Starting Search Orders By Email **********")
        searchorder = SearchOrder(self.driver)
        searchorder.clickOnSalesMenu()
        searchorder.clickOnOrderMenu()

        self.logger.info("************* searching order by email **********")
        searchorder.setEmail("james_pan@nopCommerce.com")
        searchorder.clickSearch()
        time.sleep(5)
        status = searchorder.searchOrderByEmail("james_pan@nopCommerce.com")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchOrderByEmail_006 Finished  *********** ")

