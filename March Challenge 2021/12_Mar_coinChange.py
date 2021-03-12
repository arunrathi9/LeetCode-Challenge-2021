"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""


class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        else:
            coins.sort(reverse=True)
            coin_count = 0
            while (amount>0):
                for i in range(len(coins)):
                    if amount >= coins[i]:
                        amount -= coins[i]
                        coin_count += 1
                        break
                    if i==len(coins)-1:
                        amount -= coins[i]
            
            result = coin_count if amount==0 else -1
            return result

sol = Solution()
print(sol.coinChange([1,2,5], 11))
print(sol.coinChange([2], 3))
print(sol.coinChange([1], 0))
print(sol.coinChange([1], 1))
print(sol.coinChange([1], 2))
print(sol.coinChange([2,5,10,1], 27))