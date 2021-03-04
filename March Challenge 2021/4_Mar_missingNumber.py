"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

"""

class solution:
    def missingNumber(self, nums):
        corr_set = set(range(len(nums)+1))
        return int(*corr_set.difference(set(nums)))

    def missingNumber2(self, nums):
        expected = len(nums)*(len(nums)+1)/2
        actual= sum(nums)
        return int(expected - actual)



sol = solution()
print(sol.missingNumber([0,1,3]))
print(sol.missingNumber([0]))
print(sol.missingNumber([0,1]))