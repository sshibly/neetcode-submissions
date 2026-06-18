class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        
        # removes the smallest elements until only the k largest remain
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # removes the smallest elements until only the k largest remain
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

        
