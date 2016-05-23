# -*- coding: utf-8 -*-
""" Unit test file """

__author__ = 'ShashankSi'

import unittest
from TestBase import set_browser
import SeleniumValidation
import SeleniumCommonActions
from ddt import ddt, data, unpack
import xlrd


def getData(fileName):
    myrows = []
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    for row_index in range(1, sheet.nrows):
        myrows.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
    return myrows

@ddt
class MyTestCase(unittest.TestCase):
    """ Test Class """

    @data(*getData(r"C:\Users\ajaygi\Desktop\MERGEDColorbox\TestData.xlsx"))
    @unpack
    def test_esri_app(self, URL):
        """ Test Method """

        # Launch the browser
        #   self.driver.get("http://cmsqa.esri.com/data/data-maps/data-and-maps-server")
        self.driver.get(URL)

        #   Check class 'fancybox-skin' is present

        if SeleniumValidation.check_fancybox_class(self.driver):

            print ("1: Class 'fancybox-skin' is not visible")

            #   Perform Rich Data Actions
            SeleniumCommonActions.action_on_richdata(self.driver)
        else:
            print ("Class 'fancybox-skin' is visible")
            assert False


        #   Check class 'fancybox-skin' is present
        if SeleniumValidation.check_fancybox_class(self.driver):
            print ("2: Class 'fancybox-skin' is not visible")
            assert True
        else:
            print ("Class 'fancybox-skin' is visible")
            assert False


    @classmethod
    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        """ Quit browser"""
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
