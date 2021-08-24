#importing modules
from collections import deque

# Definition for a Node.
class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'TreeNode'):
        if root == None:
            return []
        result = []
        d = deque([root])
        while(d):
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                level.append(cur.val)
                for child in cur.children:
                    q.append(child.val)
            result.append(level)
        return result

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

sol = Solution()
print(sol.levelOrder(root))