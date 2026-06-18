class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for n in nums:
            res = n ^ res # XOR 
        return res

        # time: O(n)
        # space: O(1)
        