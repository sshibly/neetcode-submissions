class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        totalNum = n * n 

        freqMap = defaultdict(int)

        for i in range(1, totalNum + 1):
            freqMap[i] = 0
        
   
        for r in range(n):
            for c in range(n):
                if grid[r][c] in freqMap:
                    freqMap[grid[r][c]] += 1
        
        res = []
        for k, v in freqMap.items():
            if v == 2:
                res.append(k)

        for k, v in freqMap.items():
            if v == 0:
                res.append(k)
        
        return res




        

