class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time

        # freq map of tasks { A:3, B:2, C:2}
        count = Counter(tasks)

        # negate count for max heap
        maxHeap = [-c for c in count.values()]

        # convert list to heap in lienar time O(n)
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pair of [-cnt, idleTime]

        # as long as one of these is non-empty
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                # if count is nonzero
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time

        




