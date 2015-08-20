from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest
import sys



class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_search_for_a_p_and_p_location(self):
		# Marco has heard about a cool new app for finding
		# pastries in parks.
		self.browser.get('http://localhost:8000')

		# They notice the page title and header mention
		# a pastry in a parks
		self.assertIn('Pastry in a Park', self.browser.title)


		# They see a map
		self.browser.find_element_by_id('pastry_map')


		# And above the map, they are invited to enter a
		# location to begin their pastry and park search
		inputbox = self.browser.find_element_by_id('location_search_box')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a location')

		# They enter their desired location
		inputbox.send_keys('11 W 53rd St, New York, NY 110019')
		inputbox.send_keys(Keys.ENTER)
		# And the page updates the map with their search
		# results.

		#self.fail('Finish test')

		# Satisfied, they go back to sleep.


	def test_layout_and_styling(self):
		self.browser.get('http://localhost:8000')
		self.browser.set_window_size(1024, 768)
		inputbox = self.browser.find_element_by_id('location_search_box')
		self.browser.implicitly_wait(3)
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5)

if __name__ == '__main__':
	unittest.main()





