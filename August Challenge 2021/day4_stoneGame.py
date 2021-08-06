class Solution:
    def stoneGame(self, piles) -> bool:
        a = piles[0]
        b = piles[-1]
        arr = piles
        sum1 = 0 #first player
        sum2 = 0 #second player
        l = len(piles)
        for i in range(l-1):
            if i%2==0:
                if a==b:
                    temp = True if arr[1] < arr[-2] else False
                    if(temp):
                        sum1 += a
                    else:
                        sum1 += b

                elif a>b:
                    sum1 += a
                    arr = arr[1:]
                    a = arr[0]
                else:
                    sum1 += b
                    arr = arr[:-1]
                    b = arr[-1]
            else:
                if a>=b:
                    sum2 += a
                    arr = arr[1:]
                    a = arr[0]
                else:
                    sum2 += b
                    arr = arr[:-1]
                    b = arr[-1]
        sum2 += arr[0]
        return True if sum1>sum2 else False

sol = Solution()
print(sol.stoneGame([5,3,4,5])) 
print(sol.stoneGame([3,7,2,3])) 