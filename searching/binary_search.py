
class BinarySearch:
    """Binary Search algorithms."""

    def rank(self, k, arr):
        """Look for value k in array arr. Return index of k; otherwise -1."""

        # arr must be sorted
        if not(arr[0] < arr[len(arr)//2] < arr[len(arr)-1]):
            raise ValueError("Array must be sorted")

        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if k < arr[mid]:
                hi = mid - 1
            elif k > arr[mid]:
                lo = mid + 1
            else:
                return mid

        return -1
