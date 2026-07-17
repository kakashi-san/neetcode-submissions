from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh_count = 0
        rotten = []
        fresh = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c, 0))
                if grid[r][c] == 1:
                    fresh_count += 1

        q = deque(rotten)

        time = 0

        while q:
            q_len = len(q)
            for _ in range(q_len):
                popped = q.popleft()
                x, y, time = popped
                for (dx, dy) in [
                        (0, 1),
                        (1, 0),
                        (-1, 0),
                        (0, -1)
                        ]:
                    if 0 <= x + dx < ROWS and 0 <= y + dy < COLS and grid[x + dx][y + dy] == 1:
                        grid[x +  dx][y + dy] =  2
                        fresh_count -= 1
                        q.append((x + dx, y + dy, time + 1))

        if fresh_count > 0:
            return -1
        return time

        

