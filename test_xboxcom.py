#!/usr/bin/env python3

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture()
def setup(request):
    
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    request.instance.driver = driver
    wait = WebDriverWait(driver, 10)

    yield driver
    
    print("closing chrome driver")
    driver.close()

# .usefixutres is the same as applying this to every TestMethod
@pytest.mark.usefixtures("setup")
class TestXbox:

    def test_XboxHomepage_NotLoggedIn(self):

        self.driver.get('http://www.xbox.com')
        assert 'Xbox' in self.driver.title

        # Find the Xbox logo graphic
        try:
            xboxLogoImg = self.driver.find_element_by_id('uhfCatLogo')
        except NoSuchElementException:
            print("id 'uhfCatLogo' does not exist")

        try:
            loginBtn = self.driver.find_element_by_id('mectrl_headerPicture')
        except NoSuchElementException:
            print("id 'mectrl_headerPicture' does not exist")

    def test_XboxSeriesX_PreOrderBtn(self):

        self.driver.get('https://xbox.com/en-US/consoles/xbox-series-x')
        assert 'Xbox Series X' in self.driver.title

        try:
            preOrderBtn = self.driver.find_element_by_class_name('purchButtonPB')
        except NoSuchElementException:
            print("id 'purchButtonPB' does not exist")


