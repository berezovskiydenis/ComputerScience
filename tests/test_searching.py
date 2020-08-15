import unittest

from searching.binary_search import BinarySearch


class Test_Searching(unittest.TestCase):
    def test_binary_search(self):
        l = [10, 11, 12, 16, 18, 23, 29, 33, 48, 54, 57, 68, 77, 84, 98]
        bs = BinarySearch()
        result = bs.rank(12, l)
        self.assertEqual(result, 2)
