# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                # Append everything on all left subtrees
                stack.append(curr)
                curr = curr.left
            # pop most recently added node from stack
            curr = stack.pop()
            k -= 1 # iterate k
            if k == 0:
                # return val if we've satisfied k
                return curr.val
            # move to the right subtree of this node.
            curr = curr.right
