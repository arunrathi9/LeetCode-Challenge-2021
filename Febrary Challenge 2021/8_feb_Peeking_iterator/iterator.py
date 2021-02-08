# Below is the interface for Iterator, which is already defined for you.

class iterator2:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        print('hi1')
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return True

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        return self.nums[0]
