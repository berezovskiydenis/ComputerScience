import unittest

from adt.bag import Bag


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.bg = Bag()

    def test_empty(self):
        self.assertTrue(self.bg.is_empty())

    def test_add_three_values(self):
        self.bg.add(1)
        self.bg.add(2)
        self.bg.add(3)
        self.assertEqual(self.bg.size(), 3)

    def test_iter_protocol(self):
        self.bg.add(1)
        self.bg.add(2)
        self.bg.add(3)
        self.bg.add(4)
        self.bg.add(5)

        arr = []
        for x in self.bg:
            arr.append(x)

        self.assertEqual(arr, [1, 2, 3, 4, 5])
