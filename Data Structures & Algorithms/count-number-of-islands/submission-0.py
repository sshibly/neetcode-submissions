class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def valid(r, c):
            return 0 <= r < ROWS  and 0 <= c < COLS and grid[r][c] == "1"



        def dfs(r, c):
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)


        ROWS = len(grid)
        COLS = len(grid[0])

        seen = set()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        island = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    island += 1
                    seen.add((r, c))
                    dfs(r, c)

        return island

        # time complexity: O(m * n)
        # space complexity: O(m * n)

                    

        