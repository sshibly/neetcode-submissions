class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        q = deque([(0, 0, 1)]) # r, c, length (tuple)
        seen = set((0,0)) # coordinates of square

        def valid(row, col): 
            return 0 <= row < n and 0 <= col < n and grid[r][c] == 0

        directions = [[0, -1], [0, 1], [-1, 0], [1, 0], 
                      [1, 1], [-1, -1], [-1, 1], [1, -1]]

        while q: 
            r, c, length = q.popleft()

            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    q.append((new_row, new_col, length + 1))

        return -1

        # time complexity: O(n^2) - n is number of nodes
        # space complexity: O(n^2) 
           


       

        