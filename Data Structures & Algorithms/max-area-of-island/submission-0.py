class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1

        def dfs(r, c):
            area = 1 # count current square
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    area += dfs(new_row, new_col)
            return area

        
        ROWS = len(grid) # number of rows
        COLS = len(grid[0]) # number of cols
        seen = set() # position of square (r, c)

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    max_area = max(max_area, dfs(r, c)) 
        
        return max_area

        # time complexity: O(m * n) 
        # space complexity: O(m * n)
        # - m is number of rows 
        # - n is number of columns
                


        
        






        