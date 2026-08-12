class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        freqMap = defaultdict(int)

        for r in range(n):
            for c in range(n):
                freqMap[grid[r][c]] += 1
        
        double = 0
        missing = 0

        for i in range(1, n*n+1):
            if freqMap[i] == 2:
                double = i
            if freqMap[i] == 0:
                missing = i
        
        return [double, missing]

        # time complexity: O(n^2)
        # space complexity: O(n^2)