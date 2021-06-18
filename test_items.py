import pytest
import time


def test_links(browser):
    browser.get(' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(10)
    basket = browser.find_element_by_id('add_to_basket_form')
    assert basket, 'basket not found'
