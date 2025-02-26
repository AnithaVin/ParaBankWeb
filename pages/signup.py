from selenium.webdriver.common.by import By


class signup:
    def __init__(self, driver): # construster creation
        self.driver = driver

    reg = "//a[text()='Register']" # xpath creation

    def nevagate_reg_page(self): #method creation
        self.driver.find_element(By.XPATH, self.reg)


