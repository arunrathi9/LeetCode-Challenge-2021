"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 1038: 
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

"""


class TreeNode:

    def __init__(self, val, left=None, right=None, tree_list=[]):
        self.data = val
        self.left = left
        self.right = right
        self.tree_list = tree_list

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)

            else:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)

        else:
            self.data = TreeNode(data)

    def print_tree(self):
        self.tree_list.append(self.data)

        if self.left:
            self.left.print_tree()

        if self.right:
            self.right.print_tree()

        return self.tree_list


class Solution:

    result = 0

    def greater_bst(self, node):

        def dfs(node):
            if node:
                dfs(node.right)
                self.result += node.data
                node.data = self.result
                dfs(node.left)

        dfs(node)

        return node


node_list = [1, 6, 0, 2, 5, 7, 3, 8]
#Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Tree = TreeNode(4)
for i in node_list:
    Tree.insert(i)

greater_tree = Solution()
result = greater_tree.greater_bst(Tree)
print(result.print_tree())
