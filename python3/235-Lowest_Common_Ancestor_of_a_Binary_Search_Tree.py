#Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


## BSTs are restricted by the rules: any left subtree will always have values lover than root node. Any right subtrees will have values greater than root. 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur: # keep running no matter tree size
            if p.val > cur.val and q.val > cur.val:
                # LCA must live on right subtree of cur
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                # LCA must live on left subtree of cur
                cur = cur.left
            else:
                # cur is the split between targets and is the most recent
                # ancestor so must be lowest.
                return cur
