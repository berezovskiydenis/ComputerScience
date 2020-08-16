
class Stack:
    """A stack is an collection that is based on the last-in-first-out
    (LIFO) policy.
    """

    def __init__(self):
        """Create an empty stack."""
        self.items = []
        self._counter = 0

    def push(self, item):
        """Add an item to stack."""
        self.items.append(item)

    def pop(self):
        """Remove the most recently added item."""
        return self.items.pop()

    def is_empty(self):
        """Is the stack empty."""
        return True if self.size() == 0 else False

    def size(self):
        """Number of items in the stack."""
        return len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if self.size() == self._counter:
            self._counter = 0
            raise StopIteration
        else:
            item = self.items[self._counter]
            self._counter += 1
            return item
