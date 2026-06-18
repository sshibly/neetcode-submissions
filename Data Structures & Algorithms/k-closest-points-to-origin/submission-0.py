class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        # linear time operation
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        
        # converts list to heap in O(n) time
        heapq.heapify(minHeap)
        res = []
        while k > 0:
           dist, x, y = heapq.heappop(minHeap)
           res.append([x, y])
           k -= 1
        
        return res



        