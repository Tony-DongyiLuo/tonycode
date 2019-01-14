from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        #She visits the URL and the TO-DO list is there
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        

        #She sees the input box that is centralized displayed
        inputbox = self.browser.find_element_by_id('id_new_item')
        
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 
        512, delta=5)

