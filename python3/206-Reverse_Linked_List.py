# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# This is the iterative method. OT(n), OM(1)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.__class__) 

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

head = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=None))))
soln = Solution().reverseList(head)
print(soln)
