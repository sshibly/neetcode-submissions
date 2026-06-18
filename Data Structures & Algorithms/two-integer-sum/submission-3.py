class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # key: num, value: index
        # map = {3:0, 4:1, 5:2, 6:3}

        for i, num in enumerate(nums): # [3, 4, 5, 6]
            complement = target - num # 7 - 4 = 3
            if complement in map:
                return [map[complement], i] # [0, 1]
            map[num] = i #{3:0,}
        
        return []

        # time complexity: O(n)
        # space complexity: O(n)
