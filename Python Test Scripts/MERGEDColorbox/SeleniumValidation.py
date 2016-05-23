# -*- coding: utf-8 -*-
""" Validation for test scripts"""
__author__ = 'ShashankSi'


def check_fancybox_class(driver):
    """  Method to check whether the fancybox-skin is exist or not """
    try:
        fancyboxlist = driver.find_elements_by_class_name('fancybox-skin')

        #   Validate result
        if len(fancyboxlist) == 0:
            return True
        else:
            return False
    except Exception:
        return False
