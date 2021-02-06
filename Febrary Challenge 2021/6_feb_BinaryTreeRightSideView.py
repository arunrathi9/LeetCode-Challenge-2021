"""
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /  \\
2     3         <---
 \    \\
  5     4       <---
  """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res, stk = [], root and [root]
        print(stk)
        while stk:
            res.append(stk[-1].val)
            stk = [c for n in stk for c in (n.left, n.right) if c]
        return res

        stack = []
        node_level = 0
        level = 0
        sol = []
        node = root
        while True:
            while node:
                stack.append([node, node_level])
                if node_level >= level:
                    sol.append(node.val)
                    level += 1
                node = node.right
                node_level += 1
            if not stack:
                break
            node, node_level = stack.pop()
            node = node.left
            node_level += 1
        return sol


Solution.rightSideView([1, 2, 3, null, 5, null, 4])
