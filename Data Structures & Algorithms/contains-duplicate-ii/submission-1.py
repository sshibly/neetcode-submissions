class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        map = collections.defaultdict(int) # num:index
        
        # [1, 2, 3, 1]
        #           ^
        for i, num in enumerate(nums):
            if num in map and (abs(map[num] - i) <= k):
                return True
            else:
                map[num] = i # {1:0, 2:1, 3:2,  }
        
        return False

        # time: O(n)
        # space: O(n)
            

        
        