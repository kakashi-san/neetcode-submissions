class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(i,j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS: 
                return

            if grid[i][j] == "0":
                return 
            
            if grid[i][j] == "1":
                grid[i][j] = "0"
            
            bfs(i + 1, j)
            bfs(i - 1, j)
            bfs(i, j - 1)
            bfs(i, j + 1)

            return

        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        
        return count