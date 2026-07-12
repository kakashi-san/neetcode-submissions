from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(i, j):
            q = deque([(i,j)])
            grid[i][j] = '0'

            while q:
                pop_len = len(q)
                for _ in range(pop_len):
                    x, y = q.popleft()
                    for (dx, dy) in [
                        (1, 0), (0, 1), (-1, 0), (0, -1)
                        ]:
                        if x + dx >= 0 and x + dx < ROWS and y + dy >= 0 and y + dy < COLS:
                            if grid[x + dx][y + dy] == "1":
                                q.append((x + dx, y + dy))
                                grid[x + dx][y + dy] = "0" 

        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1

        return count