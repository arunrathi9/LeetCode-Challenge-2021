# Definition for a Linked list Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head):

        curr = head
        while curr != None:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = curr.next.next

        curr = head
        while curr != None:
            curr.next.random = curr.random
            curr = curr.next.next

        curr = head
        curr_copy = head.next
        while curr.next != None:
            temp = curr.next
            curr.next = curr.next.next
            curr = temp

        return curr, curr_copy

    def print_copylist(self, curr):
        while curr != None:
            if curr.random != None and curr.next != None:
                print(
                    f"Data: {curr.val} - Next: {curr.next.val} - Random: {curr.random.val}")
            elif curr.random == None and curr.next == None:
                print(f"Data: {curr.val} - Next: None - Random: None")
            elif curr.random == None:
                print(
                    f"Data: {curr.val} - Next: {curr.next.val} - Random: None")
            else:
                print(
                    f"Data: {curr.val} - Next: None - Random: {curr.random.val}")

            curr = curr.next

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


sol = Solution()
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)
# sol.print_copylist(head)

head.random = Node(10002)
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head
# sol.print_copylist(head)

# sol.print_copylist(head)
result1, r2 = sol.copyRandomList(head)
print(sol.print_copylist(r2))
