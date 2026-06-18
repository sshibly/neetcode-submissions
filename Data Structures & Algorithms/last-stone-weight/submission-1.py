class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negate values in stones
        stones = [-s for s in stones]

        # convert list to heap in O(n)
        heapq.heapify(stones)

        # we run simulation until it's <= 1
        while len(stones) > 1:
            # removes first and second largest stones 
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            
            # first = -8 , second = -7
            if first > second:
                heapq.heappush(stones, second - first)

        stones.append(0)
        return abs(stones[0])








        