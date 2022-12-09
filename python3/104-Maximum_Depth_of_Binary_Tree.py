# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class RecursiveSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Essentially a fancy way of adding 1 for each iteration to a lower level.
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

class IterativeSolution:
    # Called Depth-First Search
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res

# Example 1
root = [3,9,20,null,null,15,7]
