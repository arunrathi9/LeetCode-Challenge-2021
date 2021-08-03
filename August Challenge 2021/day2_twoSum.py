# Time: O(n)
# Space: O(n)

class Solution2:
    def twoSum(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in d:
                return [d[temp], i]
            else:
                d[nums[i]] = i
print('Solution 2 : ')
sol2 = Solution2()
print(sol2.twoSum([2,7,11,19], 9))
print(sol2.twoSum([3,2,4], 6))
        
# Time: O(n^2)
# Space: O(1)
# it's a brute force method
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (target-nums[i]-nums[j])==0:
                    return [i,j]

#sol = Solution()
#print(sol.twoSum([2,7,11,19], 9))
#print(sol.twoSum([3,2,4], 6))