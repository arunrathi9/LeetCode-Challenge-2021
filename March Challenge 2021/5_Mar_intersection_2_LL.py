"""
Write a program to find the node at which the intersection of two singly linked lists begins.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        return set(headA).intersection(set(headB))

for i in [4,1,8,4,5]:
    pass
sol = Solution()
print(sol.getIntersectionNode())