class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        curSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curSum = 0

            curSum += nums[i]
            res = max(res, curSum)
        
        return res

        # time complexity: O(n)
        # space complexity: O(1)

        