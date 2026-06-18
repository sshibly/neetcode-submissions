class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        # work our way backwards in input array
        for i in range(len(nums) - 1, -1, -1):
            # nums[i] is jump length
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False
        
        # time complexity: O(n)
        # space complexity: O(1)

        