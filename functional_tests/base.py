import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.live_server_url = 'http://www.tonycodetest.site'
        super().setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        
        super().tearDownClass() 
    
    def setUp(self):
        self.opts = webdriver.FirefoxOptions()
        self.opts.add_argument("--headless")

        self.browser = webdriver.Firefox(firefox_options=self.opts)
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

