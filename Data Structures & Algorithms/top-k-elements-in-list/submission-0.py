class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        map = defaultdict(int) #[num:freq]

        for num in nums:
            map[num] += 1
        
        #[1:1, 2:2]
        for i in range(k): # 2
            map_values = list(map.values()) # [1, 2]
            max_val = max(map_values) # 2
            
            for num, freq in map.items():
                if freq == max_val: # 2
                    result.append(num) #[3, 2]
                    del map[num] # [1:1]
                    break
        
        return result
            

        