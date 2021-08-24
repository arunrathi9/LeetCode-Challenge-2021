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