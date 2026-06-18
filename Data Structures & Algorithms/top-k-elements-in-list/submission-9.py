import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the occurences of each value
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1
        
        minheap = []
        for key, val in map.items():
            heapq.heappush(minheap, (val, key))
            while len(minheap) > k:
                heapq.heappop(minheap)
        
        res = []
        for i in range(k):
            val, key = heapq.heappop(minheap)
            res.append(key)
        
        return res

        # time complexity: O(n log k)
        # space complexity: O(n + k)
        # n is the length of array
        # k is number of top k frequent elements


        

        
