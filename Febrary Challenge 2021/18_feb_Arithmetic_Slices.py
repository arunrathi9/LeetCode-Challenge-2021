"""
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference
between any two consecutive elements is the same.

example: A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

"""


class Solution():

    def is_arithmetic(self, A):

        curr_len = 0
        result_len = 0

        for i in range(2, len(A)):
            if A[i-1]-A[i-2] == A[i]-A[i-1]:
                curr_len += 1
                result_len += curr_len
            else:
                curr_len = 0

        return result_len


sol = Solution()
print(sol.is_arithmetic([1, 2, 3, 4]))
