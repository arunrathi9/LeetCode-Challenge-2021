"""
Shortest Path in Binary Matrix:

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of
cells C_1, C_2, ..., C_k such that:

    Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
    C_1 is at location (0, 0) (ie. has value grid[0][0])
    C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
    If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
    
    Return the length of the shortest such clear path from top-left to bottom-right.
    If such a path does not exist, return -1.


"""
from collections import deque


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class queueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt
        self.dist = dist


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        self.grid = grid
        n = len(self.grid)
        if self.grid[0][0] != 0 or self.grid[n-1][n-1] != 0:
            return -1

        visited = [[False for i in range(n)] for j in range(n)]
        visited[0][0] = True

        row_num = [1, 0, 1, -1, -1, -1, 0, 1]
        col_num = [1, 1, 0, 1, 0, -1, -1, -1]

        row = 0
        col = 0

        q = deque()
        s = queueNode(Point(row, col), 1)
        q.append(s)

        while q:

            curr = q.popleft()
            point = curr.pt
            if point.x == n-1 and point.y == n-1:
                return curr.dist

            for i in range(8):
                row = point.x + row_num[i]
                col = point.y + col_num[i]

                if row >= 0 and row < n and col >= 0 and col < n:
                    if self.grid[row][col] == 0 and not visited[row][col]:
                        visited[row][col] = True
                        adjcell = queueNode(Point(row, col), curr.dist+1)
                        q.append(adjcell)
        return -1


mat = [[0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0, 0], [
    0, 0, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0]]
sol = Solution()
print(sol.shortestPathBinaryMatrix(mat))
