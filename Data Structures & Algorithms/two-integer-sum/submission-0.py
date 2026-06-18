class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # val: index

        # [3, 4, 5, 6]
        #     ^
        for i, n in enumerate(nums): 
            diff = target - n # 7 - 4 = 3
            if diff in map: #[3:0, ]
                return [map[diff], i] #[0, 1]
            map[n] = i # [3:0, ]
        

        return; 
        