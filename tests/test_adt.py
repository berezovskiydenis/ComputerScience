import unittest

from adt.bag import Bag
from adt.fifo_queue import FIFOQueue
from adt.stack import Stack


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


class Test_FIFOQueue(unittest.TestCase):
    def setUp(self):
        self.q = FIFOQueue()

    def test_empty(self):
        self.assertTrue(self.q.is_empty())

    def test_zero_size(self):
        self.assertEqual(self.q.size(), 0)

    def test_add_items(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.assertEqual(self.q.size(), 3)
        self.assertFalse(self.q.is_empty())

    def test_add_remove_items(self):
        self.q.enqueue(0)
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(4)
        self.assertEqual(self.q.size(), 5)
        i = self.q.dequeue()
        self.assertEqual(i, 0)
        self.assertEqual(self.q.size(), 4)

    def test_deque(self):
        self.q.enqueue(0)
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.assertEqual(self.q.size(), 3)
        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()
        self.assertRaises(ValueError, self.q.dequeue)
        self.assertEqual(self.q.size(), 0)
        self.assertTrue(self.q.is_empty())

    def test_non_zero_size(self):
        self.q.enqueue(0)
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.dequeue()
        self.q.dequeue()
        self.q.enqueue(3)
        self.assertEqual(self.q.size(), 2)


class Test_Stack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_add_items(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)

    def test_pop_item(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        item = self.stack.pop()
        self.assertEqual(item, 3)
        self.assertEqual(self.stack.size(), 2)
