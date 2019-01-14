from unittest import skip
from .base import FunctionalTest



class ItemValidationTest(FunctionalTest):
    
    
    def test_cannot_add_empty_list_items(self):
        #The user submits an empty list item
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #The error message shows the list item cannot be empty
        error = self.browser.find_element_by_css_selector('.has_error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #The user submits a normal list item and it works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        #The user submits an empty list item again
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #The user sees the error message again
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has_error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #Input the characters and it works
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')


