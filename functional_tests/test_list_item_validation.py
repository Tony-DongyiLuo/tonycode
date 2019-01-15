from unittest import skip
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time

class ItemValidationTest(FunctionalTest):
    
    
    def test_cannot_add_empty_list_items(self):
        #The user submits an empty list item
        self.browser.get(self.live_server_url)
        #print(len(self.browser.find_element_by_id('id_new_item').text))
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        time.sleep(5)
        print(self.browser.find_element_by_css_selector('.row').text + 'Error')

        #The error message shows the list item cannot be empty
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #The user submits a normal list item and it works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        #The user submits an empty list item again
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #The user sees the error message again
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #Input the characters and it works
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')


