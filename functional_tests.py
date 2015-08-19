from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest



class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

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
		self.fail('Finish test')
		# They enter their desired location

		# And the page updates the map with their search
		# results.

		# Satisfied, they go back to sleep.

if __name__ == '__main__':
	unittest.main()