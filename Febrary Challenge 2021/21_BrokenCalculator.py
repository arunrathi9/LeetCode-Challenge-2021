"""
On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

Example1: Input: X = 2, Y = 3 Output: 2
Example2: Input: X = 5, Y = 8 Output: 2 Explanation:{5 -> 4 -> 8}
"""


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:

        step = 0
        while X != Y:
            if X > Y:
                step += X-Y
                X = Y
            else:
                step += Y % 2 + 1
                Y = Y/2 if Y % 2 == 0 else (Y+1)/2
        return int(step)


sol = Solution()
print(sol.brokenCalc(1024, 1))
print(sol.brokenCalc(2, 3))
print(sol.brokenCalc(5, 8))
print(sol.brokenCalc(1, 1000000000))
