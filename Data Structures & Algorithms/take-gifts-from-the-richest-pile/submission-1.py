import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        heapq.heapify_max(gifts)

        while k > 0:
          curr = heapq.heappop_max(gifts)
          currSquare = math.sqrt(curr)
          heapq.heappush_max(gifts, math.floor(currSquare))
          k -= 1
        
        return sum(gifts)



        