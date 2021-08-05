# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = []

    def pathSum(self, root: TreeNode, targetSum: int, path = [], sum: int = 0):
        if (root == None):
            return None

        sum = sum + root.val
        path.append(root.val)

        if root.left == None and root.right == None:
            if sum == targetSum:
                self.result.append(path.copy())
        else:
            if(root.left):
                self.pathSum(root.left, targetSum, path, sum)
                
            if(root.right):
                self.pathSum(root.right, targetSum, path, sum)
                
        path.pop()

        return self.result


root = TreeNode(5)
root.right = TreeNode(8)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(18)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

targetSum = 22

sol = Solution()
sol.pathSum(root, targetSum)