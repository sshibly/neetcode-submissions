class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap =  nums
        # convert list to heap in O(n) time
        heapq.heapify(minHeap) 
        # [1, 2, 3, 4, 5]

        # shrink the heap until it reaches k
        while len(minHeap) > k: # 2 > 2
            heapq.heappop(minHeap)
        # [4, 5]
        
        # return the root (kth largest element)
        return minHeap[0]

        # time complexity: O(nlogk)
        # space complexity: O(k)
        # n is length of array nums, k is size of heap






        