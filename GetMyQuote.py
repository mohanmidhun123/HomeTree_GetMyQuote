
'''Automated Testing to verify "HOMETREE Website- Get My Quote Functionality"

Below is the code for doing automated testing using Selenium and Python.

'''

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class GetMyQuote(unittest.TestCase):

    #*************************************Basic Setup and Teardown for the test*********************************'''
    def setUp(self):
        self.delay = lambda: time.sleep(5)
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-local-storage")
        chrome_driver = "C://Users//Nidhi//Documents//chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        self.delay()
        self.driver.get("https://www.hometree.co.uk/")
        self.delay()
        self.driver.execute_script("window.scrollTo(0, 700)")
        Quote_button = self.driver.find_element_by_xpath("(//BUTTON[@type='button'])[5]")
        Quote_button.click()

        self.QuotePage={
            "name" : '//*[@id="ht-2d8eoQkd5CyIcQKyEuKKEC"]',
            "contact" : '//*[@id="ht-6nYDU1oapakeCSICEOsmgk"]',
            "email" : '//*[@id="ht-22sd7B4HaIAIAEi2mswG8q"]',
            "postcode" : '//*[@id="ht-47vpnrbU88weekY4sWY8aU"]',
            "submitForm": "//SPAN[@class='ht-button-text '][text()='Submit']",
            "closeForm": "(//BUTTON[@type='button'])[6]",
            "submitError": "//DIV[@class='ht-form-error ht-error'][text()='Please complete all the fields.']",
            "labelName": "//LABEL[@for='ht-2d8eoQkd5CyIcQKyEuKKEC'][text()='Please enter your name']",
            "labelContact": "//LABEL[@for='ht-6nYDU1oapakeCSICEOsmgk'][text()='Please enter a valid 11 digit phone number']",
            "labelEmail": "//LABEL[@for='ht-22sd7B4HaIAIAEi2mswG8q'][text()='Please enter a valid e-mail address']",
            "labelPostcode": "//LABEL[@for='ht-47vpnrbU88weekY4sWY8aU'][text()='Please enter your postcode']"
        }
        self.Success={
            "name" : "Midhun",
            "contact" : "09958044059",
            "email" : "poojasatheesh1992@gmail.com",
            "postcode" : "SL12QD"
        }
        self.Failure={
            "name" : "Midhun",
            "contact" : "09958044",
            "email" : "midhun.com",
            "postcode" : ""
        }
    def tearDown(self):
        #To tear down the session
        self.driver.quit()


    # ************************************* 1. To Verify if the Get My Quote form can be submitted with relevant details *********************************'''
    def test_1(self):
        try:
            self.driver.find_element_by_xpath(self.QuotePage.get("name")).send_keys(self.Success.get("name"))
            self.driver.find_element_by_xpath(self.QuotePage.get("contact")).send_keys(self.Success.get("contact"))
            self.driver.find_element_by_xpath(self.QuotePage.get("email")).send_keys(self.Success.get("email"))
            self.driver.find_element_by_xpath(self.QuotePage.get("postcode")).send_keys(self.Success.get("postcode"))
            self.delay()
            self.driver.find_element_by_xpath(self.QuotePage.get("submitForm")).click()
            element = self.driver.find_element_by_xpath(self.driver.find_element_by_xpath(self.QuotePage.get("submitError")))
            if element.is_displayed():
                print("Element found")
                self.assertTrue(True)
            else:
                print("Element not found")
                self.assertTrue(False)

        except Exception as e:
            raise e

    # ************************************* 2. To Verify if the Get My Quote form can be closed. *********************************'''
    def test_2(self):
        try:
            self.driver.find_element_by_xpath(self.QuotePage.get("closeForm")).click()
            element = self.driver.find_element_by_xpath(self.QuotePage.get("name"))
            if element.is_displayed():
                print("Element found")
                self.assertTrue(False)
            else:
                print("Element not found")
                self.assertTrue(True)

        except Exception as e:
            raise e

    # ************************************* 3. To Verify if the NAME field notifies the user to fill the name *********************************'''
    def test_3(self):
        try:
            x = self.driver.find_element_by_xpath(self.QuotePage.get("name")).send_keys(self.Failure.get("name"))
            self.delay()
            element = self.driver.find_element_by_xpath(self.QuotePage.get("labelName"))
            if element.is_displayed():
              print ("Element found")
              self.assertTrue(False)
            else:
              print ("Element not found")
              self.assertTrue(True)
            self.driver.find_element_by_xpath(self.QuotePage.get("name")).clear()
            self.driver.find_element_by_xpath(self.QuotePage.get("name")).send_keys(Keys.RETURN)
            self.delay()

            if element.is_displayed():
              print ("Element found")
              self.assertTrue(True)
            else:
              print ("Element not found")
              self.assertTrue(False)

        except Exception as e:
            raise e

    # ************************************* 4. To Verify if the Contact field notifies the user to enter valid 11 digit number *********************************'''
    def test_4(self):
        try:
            x = self.driver.find_element_by_xpath(self.QuotePage.get("contact")).send_keys(self.Failure.get("contact"))
            self.delay()
            element = self.driver.find_element_by_xpath(self.QuotePage.get("labelContact"))
            if element.is_displayed():
              print ("Element found")
              self.assertTrue(False)
            else:
              print ("Element not found")
              self.assertTrue(True)
            self.driver.find_element_by_xpath(self.QuotePage.get("contact")).send_keys(Keys.RETURN)
            self.delay()

            if element.is_displayed():
              print ("Element found")
              self.assertTrue(True)
            else:
              print ("Element not found")
              self.assertTrue(False)
        except Exception as e:
            raise e

    # ************************************* 5. To Verify if the Contact field notifies the user to enter valid a valid email address *********************************'''
    def test_5(self):
         try:
             x = self.driver.find_element_by_xpath(self.QuotePage.get("email")).send_keys(self.Failure.get("email"))
             self.delay()
             Name = self.driver.find_element_by_xpath(self.QuotePage.get("labelEmail"))
             if Name.is_displayed():
               print ("Element found")
               self.assertTrue(False)
             else:
               print ("Element not found")
               self.assertTrue(True)
             self.driver.find_element_by_xpath(self.QuotePage.get("email")).send_keys(Keys.RETURN)
             self.delay()

             if Name.is_displayed():
               print ("Element found")
               self.assertTrue(True)
             else:
               print ("Element not found")
               self.assertTrue(False)
         except Exception as e:
            raise e

    # ************************************* 5. To Verify if the Contact field notifies the user to enter valid a valid postcode *********************************'''
    def test_6(self):
        try:
            self.delay()
            element = self.driver.find_element_by_xpath(self.QuotePage.get("labelPostcode"))
            if element.is_displayed():
              print ("Element found")
              self.assertTrue(False)
            else:
              print ("Element not found")
              self.assertTrue(True)
            self.delay()
            self.driver.find_element_by_xpath(self.QuotePage.get("postcode")).send_keys(Keys.RETURN)
            if element.is_displayed():
              print ("Element found")
              self.assertTrue(True)
            else:
              print ("Element not found")
              self.assertTrue(False)
        except Exception as e:
            raise e



if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(GetMyQuote)
        unittest.TextTestRunner(verbosity=2).run(suite)