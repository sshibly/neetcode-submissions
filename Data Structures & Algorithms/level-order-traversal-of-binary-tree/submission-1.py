# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        
        res = []
        sublist = []

        while len(queue) > 0:
            sublist = []
            for i in range(len(queue)): # i = 4, len = 4
                curr = queue.popleft()   # curr = 7, queue = []
                sublist.append(curr.val) # [4, 5, 6, 7]
                if curr.left:
                    queue.append(curr.left) # queue = [4, 5, 6]
                if curr.right:
                    queue.append(curr.right) # queue = [4, 5, 6, 7]
            
            res.append(sublist) # res = [[1], [2, 3], [4, 5, 6, 7]]
        

        return res

        # time complexity: O(n)
        # space complexity: O(n)
                



        