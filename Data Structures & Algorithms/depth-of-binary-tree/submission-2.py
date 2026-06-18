# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

        # time complexity: O(n) n is number of nodes
        # space complexity: O(h) h is height of tree
        # best case - O(log n) - balanced tree
        # worst case - O(n) - unbalanced tree