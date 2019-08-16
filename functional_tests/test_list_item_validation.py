from unittest import skip
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time

class ItemValidationTest(FunctionalTest):
    
    #@skip
    def test_cannot_add_empty_list_items(self):
        #The user submits an empty list item
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        time.sleep(5)

        #The error message shows the list item cannot be empty
        #error = self.browser.find_element_by_css_selector('.has-error')
        error = self.browser.find_element_by_css_selector('#id_text:invalid')
        #self.assertEqual(error.text, "You can't have an empty list item")
        self.assertEqual(error.text, "")

        #The user submits a normal list item and it works
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        #The user submits an empty list item again
        self.get_item_input_box().send_keys('\n')

        #The user sees the error message again
        self.check_for_row_in_list_table('1: Buy milk')
        #error = self.browser.find_element_by_css_selector('.has-error')
        error = self.browser.find_element_by_css_selector('#id_text:invalid')
        #self.assertEqual(error.text, "You can't have an empty list item")
        self.assertEqual(error.text, "")

        #Input the characters and it works
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(5)
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')


