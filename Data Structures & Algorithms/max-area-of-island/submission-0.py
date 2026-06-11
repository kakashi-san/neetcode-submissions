class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(i, j):
            if i < 0  or i >= ROWS or j < 0 or j >= COLS:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            return (
            1 + bfs(i + 1, j)
            + bfs(i, j + 1)
            + bfs(i - 1, j)
            + bfs(i, j - 1)
            )
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = bfs(r, c)
                    max_area = max(count, max_area)

        return max_area