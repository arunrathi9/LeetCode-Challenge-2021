"""
Given the integer array candyType of length n, return the maximum number of different types of
candies she can eat if she only eats n / 2 of them.

Input: candyType = [1,1,2,2,3,3]
Output: 3
"""

class Solution:
    def distributeCandies(self, candyType):
        """Return the maximum number of different types of 
        candies she can eat if she only eats n / 2 of them.

        :param candyType: array
        :type candyType: list
        :rtype: int
        :return: maximum number of different types of candies one can eat
        """
        n = len(candyType)//2
        candy_types = len(set(candyType))
        return n if n<=candy_types else candy_types


sol = Solution()
print(sol.distributeCandies([1,1,2,2,3,3]))
print(sol.distributeCandies([1,1,2,3]))
print(sol.distributeCandies([1,1,1,1]))
print(sol.distributeCandies([1,2,3,4]))     

        