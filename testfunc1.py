import func1
import unittest

class TestFuncs(unittest.TestCase):

    # Exercice 1.1
    def test_max_int(self):
        # Test liste vide et liste non vide
        self.assertEqual(func1.max_list_int([]), 0)
        self.assertEqual(func1.max_list_int([1, 2, 3, 4]), -9)

if __name__ == '__main__':
    unittest.main()
