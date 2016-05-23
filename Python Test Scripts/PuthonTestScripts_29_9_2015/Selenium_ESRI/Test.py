# -*- coding: utf-8 -*-
""" Unit test file """

__author__ = 'ShashankSi'

import unittest
from TestBase import set_browser
import SeleniumValidation
import SeleniumCommonActions


class MyTestCase(unittest.TestCase):
    """ Test Class """

    def test_esri_app(self):
        """ Test Method """

        # Launch the browser
        self.driver.get("http://cmsqa.esri.com/data/data-maps/data-and-maps-server")

        #   Check class 'fancybox-skin' is present
        if SeleniumValidation.check_fancybox_class(self.driver):

            print "1: Class 'fancybox-skin' is not visible"

            #   Perform Rich Data Actions
            SeleniumCommonActions.action_on_richdata(self.driver)
        else:
            print "Class 'fancybox-skin' is visible"
            assert False


        #   Check class 'fancybox-skin' is present
        if SeleniumValidation.check_fancybox_class(self.driver):
            print "2: Class 'fancybox-skin' is not visible"
            assert True
        else:
            print "Class 'fancybox-skin' is visible"
            assert False



    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()


    def tearDown(self):
        """ Quit browser"""
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
