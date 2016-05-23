# -*- coding: utf-8 -*-
""" Selenium action methods """
__author__ = 'ShashankSi'

import time
import SeleniumValidation

def action_on_richdata(driver):
    """ Method to perform actions on rich data"""

    # Search all the Color Box
    try:
        web_ele_colorbox_list = driver.find_elements_by_class_name("colorbox-image")
        click_and_close_richdata(driver, web_ele_colorbox_list)
    except Exception:
        print "Color box image class not present"

    # Search all the Color box content
    try:
        web_ele_colorcontent_list = driver.find_elements_by_class_name("colorbox-content")
        click_and_close_richdata(driver, web_ele_colorcontent_list)
    except Exception:
        print "Color box content class not present"

    # Search all the Color box evlarge
    try:
        web_ele_colorevlarge_list = driver.find_elements_by_class_name("colorbox-evlarge")
        click_and_close_richdata(driver, web_ele_colorevlarge_list)
    except Exception:
        print "Color box evlarge class not present"

    # Search all the Color Box evsmall
    try:
        web_ele_colorevsmall_list = driver.find_elements_by_class_name("colorbox-evsmall")
        click_and_close_richdata(driver, web_ele_colorevsmall_list)
    except Exception:
        print "Color box evsmall class not present"



def click_and_close_richdata(driver, web_list_container):
    """ Select and close rich data """

    for item in web_list_container:
        container = item.find_element_by_tag_name("img")
        container.click()

        #   Wait to laod rich data
        wait_to_load_webelement(driver)
        time.sleep(2)

        #   Validate result
        if not SeleniumValidation.check_fancybox_class(driver):
            print "fancybox-skin class is visible"
        else:
            print "fancybox-skin class in not visible"
            assert False

        #   Click on close icon
        click_on_close_icon(driver)



def click_on_close_icon(driver):
    """ Click on close icon """

    close_button = driver.find_elements_by_class_name("fancybox-close")
    for btn in close_button:
        btn.click()
        break
    time.sleep(1)



def wait_to_load_webelement(driver):
    """ Wait to load an element """

    i = 0
    while True:
        try:
            loading_element = driver.find_element_by_id("fancybox-loading")
            if loading_element.is_displayed() and i < 10:
                time.sleep(1)
                i += 1
                continue
        except Exception:
            break