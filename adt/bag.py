
class Bag:
    """Bag is a collection where removing items is not supported."""

    def __init__(self):
        """Create an empty bag."""
        self.items = []
        self._counter = 0

    def add(self, item):
        """Add an item to the bag."""
        self.items.append(item)

    def is_empty(self):
        """Check if bag is empty."""
        return True if self.size() == 0 else False

    def size(self):
        """Size of a bag."""
        return len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if self._counter == len(self.items):
            self._counter = 0
            raise StopIteration
        else:
            result = self.items[self._counter]
            self._counter += 1
            return result

