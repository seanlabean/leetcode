#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

#A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check null cases
        if not subRoot:
            return True
        if not root:
            # reached bottom of tree without True exit
            return False
        # check if same tree
        if self.isSameTree(root, subRoot):
            return True
        # recursively check left and right of root against subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
