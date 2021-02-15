"""
The K Weakest Rows in a Matrix

Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), 
return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers
in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand
in the frontier of a row, that is, always ones may appear first and then zeros.

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]
"""


class Solution:
    def kWeakestRows(self, mat, k):
        l = []
        for i in range(len(mat)):
            l.append([mat[i].count(1), i])
        l.sort()

        return [l[i][1] for i in range(len(l)) if i < k]

    def kWeakestRows2(self, mat, k):
        d = dict()

        for i, j in enumerate(mat):
            d[i] = sum(j)

        return sorted(d, key=d.get)[:k]

    def kWeakestRows3(self, mat, k):
        l = [(sum(row), i) for i, row in enumerate(mat)]
        l.sort()
        return [i for s, i in l[:k]]


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]

sol = Solution()
#print(sol.kWeakestRows(mat, 3))
#print(sol.kWeakestRows2(mat, 3))
print(sol.kWeakestRows3(mat, 3))
