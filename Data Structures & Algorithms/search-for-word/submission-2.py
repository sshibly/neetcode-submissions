class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c, i):
            # Current square doesn't match
            if not valid(r, c) or (r, c) in seen:
                return False

            if board[r][c] != word[i]:
                return False

            # Found the entire word
            if i == len(word) - 1:
                return True

            # Use this cell
            seen.add((r, c))

            # Look for the NEXT character
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc

                if dfs(new_row, new_col, i + 1):
                    return True

            # Undo choice so another path can use this cell
            seen.remove((r, c))

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False