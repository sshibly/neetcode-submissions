# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, small, large):
            # empty BST is valid 
            if not node:
                return True
            
            # current node must be inside range
            if not (small < node.val < large):
                return False

            # left subtree:
            # values must stay smaller than current node
            left = dfs(node.left, small, node.val)

            # right subtree:
            # values must stay larger than current node
            right = dfs(node.right, node.val, large)

            # both sides must be valid
            return left and right
        
        # start with infinite bounds
        return dfs(root, float("-inf"), float("inf"))

        # time complexity: O(n) n is number of nodes
        # space complexity: o(h) h is height of tree
        # O(n) - worst case - unbalanced/skewed tree
        # O(log n) - best case - balanced tree
        