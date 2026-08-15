class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
       
        ROWS = len(image)
        COLS = len(image[0])
        original = image[sr][sc]

        if original == color:
            return image
       
       
        def valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and image[r][c] == original

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            image[r][c] = color
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc
                if valid(new_row, new_col):
                    image[new_row][new_col] = color
                    dfs(new_row, new_col)
        
        dfs(sr, sc)
        return image
        
        # Time Complexity: O(m * n)
        # Space complexity: O(m * n)

        
    