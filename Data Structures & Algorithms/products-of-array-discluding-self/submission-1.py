class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_arr = []
        current_num = 1
        prefix_num = 1

        # build prefix product except current index
        # [1, 2, 4, 6]
        #           ^
        for n in nums:
            prefix_num *= current_num # 8
            prefix_arr.append(prefix_num) # [1, 1, 2, 8]
            current_num = n # 6


        postfix_arr = []
        curr_num = 1
        postfix_num = 1
        
        # build postfix product except current index
        # [6, 4, 2, 1]
        #           ^
        for n in reversed(nums):
            postfix_num *= curr_num # 48
            postfix_arr.append(postfix_num) # [1,6,24,48]
            curr_num = n # 1
        
        res = []
        
        # compute the result by multiplying prefix 
        # and postfix products at each index
        # prefix:    [1, 1, 2, 8]
        # postfix:   [48, 24, 6, 1]
        # result:    [48, 24, 12, 8]

        postfix_arr.reverse()

        for i, j in zip(prefix_arr, postfix_arr):
            res.append(i * j)
        
        return res

        # time complexity: O(n)
        # space complexity: O(n)