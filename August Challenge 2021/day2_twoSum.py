# Time: O(n^2)
# Space: O(1)

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (target-nums[i]-nums[j])==0:
                    return [i,j]

sol = Solution()
print(sol.twoSum([2,7,11,19], 9))
print(sol.twoSum([3,2,4], 6))

# Time: O(n)
# Space: O(1)

class Solution2:
    def twoSum(self, nums, target):
        pass
        