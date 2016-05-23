# -*- coding: utf-8 -*-
""" Selenium action methods """
__author__ = 'ShashankSi'

import time
import SeleniumValidation
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def action_on_richdata(driver):
    """ Method to perform actions on rich data"""
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(driver.find_elements_by_xpath("//*")))
    except:
        wait_to_load_webelement(driver,"xpath","//*")

##wait_to_load_webelement(driver,"tagname","a")

    all_elements_list = driver.find_elements_by_tag_name("a")
##    time.sleep(8)

    for item_all_elements_list in all_elements_list:
        if  str(item_all_elements_list.get_attribute("class")).split("-")[0] == 'colorbox':

            try:
                element = item_all_elements_list.find_element_by_tag_name("img")
                element.click()
##                close_button = self.driver.find_element_by_class_name("fancybox-close")
##                close_button.click()
                time.sleep(5)
            except :
                item_all_elements_list.click()
                time.sleep(5)


            wait_to_load_webelement(driver, "id", "fancybox-close")
##            time.sleep(2)

            close_button = driver.find_elements_by_class_name("fancybox-close")
            for btn in close_button:
                    btn.click()
                    break
            time.sleep(5)




##                print ("error")

    # Search all the Color Box
##    try:
##        web_ele_colorbox_list = driver.find_elements_by_class_name("colorbox-image")
##        click_and_close_richdata(driver, web_ele_colorbox_list)
##    except Exception:
##        print ("Color box image class not present")
##
##    # Search all the Color box content
##    try:
##        web_ele_colorcontent_list = driver.find_elements_by_class_name("colorbox-content")
##        click_and_close_richdata(driver, web_ele_colorcontent_list)
##    except Exception:
##        print ("Color box content class not present")
##
##    # Search all the Color box evlarge
##    try:
##        web_ele_colorevlarge_list = driver.find_elements_by_class_name("colorbox-evlarge")
##        click_and_close_richdata(driver, web_ele_colorevlarge_list)
##    except Exception:
##        print "Color box evlarge class not present"
##
##    # Search all the Color Box evsmall
##    try:
##        web_ele_colorevsmall_list = driver.find_elements_by_class_name("colorbox-evsmall")
##        click_and_close_richdata(driver, web_ele_colorevsmall_list)
##    except Exception:
####        print "Color box evsmall class not present"
##
##
##
##def click_and_close_richdata(driver, web_list_container):
##    """ Select and close rich data """
##
##    for item in web_list_container:
##        container = item.find_element_by_tag_name("img")
##        container.click()
##
##        #   Wait to laod rich data
##        wait_to_load_webelement(driver, 'id', 'fancybox-loading')
##        time.sleep(2)
##
##        #   Validate result
##        if not SeleniumValidation.check_fancybox_class(driver):
##            print ("fancybox-skin class is visible")
##        else:
##            print ("fancybox-skin class in not visible")
##            assert False
##
##        testpath = "C:/Users/ajaygi/Desktop/TESTIMAGES//" + str(datetime.datetime.now()).split(".")[1] + ".png"
##        driver.get_screenshot_as_file(testpath)
##
##
##
##
##
##        #   Click on close icon
##        click_on_close_icon(driver)
##
##
##
##def click_on_close_icon(driver):
##    """ Click on close icon """
##
##    close_button = driver.find_elements_by_class_name("fancybox-close")
##    for btn in close_button:
##        btn.click()
##        break
##    time.sleep(1)

def wait_to_load_webelement(driver, searche_attribute, search_element):
    """ Wait to load an element """

    i = 0
    while True:
        try:
            #   loading_element = driver.find_element_by_id("fancybox-loading")
            loading_element = search_ele_with_attrubite(driver, searche_attribute, search_element)
            if loading_element.is_displayed() and i < 20:
                time.sleep(1)
                i += 1
                continue
        except Exception:
            break

def search_ele_with_attrubite(driver, searche_attribute, search_element):
    if searche_attribute == 'class_name':
        return driver.find_element_by_class_name(search_element)
    elif searche_attribute == 'id':
        return driver.find_element_by_id(search_element)
    elif searche_attribute == 'tagname':
        return driver.find_elements_by_tag_name(search_element)
    elif searche_attribute == 'xpath':
        return driver.find_elements_by_xpath(search_element)