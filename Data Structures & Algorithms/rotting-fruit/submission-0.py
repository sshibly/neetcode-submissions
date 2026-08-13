class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [[-1,0], [1, 0], [0, -1], [0, 1]]

        def valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                # popping coordinates of rotten orange
                r, c = q.popleft()

                # go through all 4 adjacent spots for this orange
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc
                    # if in bounds and fresh -> make it rotten
                    if valid(new_row, new_col): 
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
                        fresh -= 1
                
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1

        # time complexity: O(m * n) 
        # space complexity: O(m * n)
        # where m is number of rows and n is number of columns




        
        