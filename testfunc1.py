import func1
import unittest

class TestFuncs(unittest.TestCase):

	def test_max_int(self):
		self.assertEqual(func1.max_list_int([1, 2, 3, 4]), 4)
		
if __name__ == '__main__':
	unittest.main()