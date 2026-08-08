class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # Start or end blocked
        if grid[0][0] != 0 or grid[ROWS - 1][COLS - 1] != 0:
            return -1

        # Single-cell grid
        if len(grid) == 1:
            return 1

        queue = deque([(0, 0, 1)])  # (row, col, path length)
        seen = {(0, 0)}

        # All 8 directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        def valid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 0

        while queue:
            r, c, length = queue.popleft()

            if r == ROWS - 1 and c == COLS - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if valid(nr, nc) and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    queue.append((nr, nc, length + 1))

        return -1
            

        