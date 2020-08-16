
class FIFOQueue:
    """FIFO queue is based on the first-in-first-out policy."""

    def __init__(self):
        """Create an empty FIFO queue."""
        self.items = []
        self._extra_items = []

    def enqueue(self, item):
        """Add an item."""
        self.items.append(item)

    def dequeue(self):
        """Remove the least recently added item."""
        if self.is_empty():
            raise ValueError("Queue is empty.")

        if len(self._extra_items) == 0:
            for x in range(len(self.items)):
                self._extra_items.append(self.items.pop())
        return self._extra_items.pop()

    def is_empty(self):
        """Is the queue empty."""
        return True if self.size() == 0 else False

    def size(self):
        """Number of items in the queue."""
        return len(self.items) + len(self._extra_items)
