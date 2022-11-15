# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # set up fast and slow pointers to find end and middle of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # define beginning of second half of list
        second = slow.next
        slow.next = None # break list in half
        
        # reverse second half of list
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
            
        # merge two lists
        first = head
        second = prev
        while second:
            tmp0, tmp1 = first.next, second.next
            first.next = second
            second.next = tmp0
            first = tmp0
            second = tmp1
