from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(i, j, visit):
            count = 1
            q = deque([(i, j)])
            visit.add((i, j))

            while q:
                pop_len = len(q)

                for _ in range(pop_len):
                    x, y = q.popleft()
                    for dx, dy in [(0, 1), (1, 0), (-1,0), (0, -1)]:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < ROWS and 0 <= ny < COLS and (nx, ny) not in visit and grid[nx][ny] == 1:
                            count += 1
                            visit.add((nx, ny))
                            q.append((nx, ny))

            return count
        
        visit = set()
        max_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == 1:
                    count = bfs(r,c, visit)
                    max_count = max(count, max_count)

        return max_count

        

