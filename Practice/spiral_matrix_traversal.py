def matrix_traversal(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    left = up = 0
    right = columns - 1
    down = rows - 1
    res = []
    while right * down >0:

        # left to right
        for i in range(left, right+1):
            res.append(matrix[up][i])

        # up to down
        for j in range(up+1, down+1):
            res.append(matrix[j][right])

        if left != right:
            for i in range(right-1, left-1, -1):
                res.append(matrix[down][i])

        if up != down:
            for j in range(down-1, up, -1):
                res.append(matrix[j][left])

        print(res)
        left += 1
        right -= 1
        up += 1
        down -= 1

    return res

mat = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix_traversal(mat))

# method 2
from math import ceil
def matrix_traversal(m):
    left = up = 0
    down = len(m)
    right = len(m[0])
    res = []
    count = ceil(len(m)/2)
    while(count>0):

        for i in range(left, right):
            res.append(m[up][i])

        for j in range(up+1, down):
            res.append(m[j][right-1])

        if left!=right:
            for i in range(right-2, left-1, -1):
                res.append(m[down-1][i])

        if up!=down:
            for j in range(down-2, up, -1):
                res.append(m[j][left])

        left += 1; up += 1
        right -= 1; down -= 1
        count -= 1
    return res

m = [[1,2,3,4,17], [5, 6,7,8,18], [9,10,11,12,19], [13,14,15,16,10],[25,24,23,22,21]]
#m = [[1]]
print(matrix_traversal(m))