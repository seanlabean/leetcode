#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.

#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]

#Input: list1 = [], list2 = [0]
#Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2: # Both lists have something to compare
            if list1.val < list2.val: # If list1 node should come next, add to dummy
                tail.next = list1
                list1 = list1.next # Increment list1
            else: # add list2 node and increment
                tail.next = list2
                list2 = list2.next
            tail = tail.next # Increment dummy list
        # At least one list does not have elements anymore.
        if list1: # if list1 still has elements, add it all to dummy
            tail.next = list1
        elif list2: # same for list2 option
            tail.next = list2
        return dummy.next
