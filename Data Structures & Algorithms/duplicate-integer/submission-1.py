class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        
        # check first, then insert
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        
        return False
        
        # time: O(n)
        # space: O(n)