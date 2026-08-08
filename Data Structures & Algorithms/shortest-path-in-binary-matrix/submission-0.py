class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Start or end blocked
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        # Single-cell grid
        if n == 1:
            return 1

        queue = deque([(0, 0, 1)])  # (row, col, path length)
        seen = {(0, 0)}

        # All 8 directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        while queue:
            r, c, length = queue.popleft()

            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n and
                    0 <= nc < n and
                    grid[nr][nc] == 0 and
                    (nr, nc) not in seen
                ):
                    seen.add((nr, nc))
                    queue.append((nr, nc, length + 1))

        return -1
            

        