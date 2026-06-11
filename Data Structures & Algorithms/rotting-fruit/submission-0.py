from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs():
            q = deque()
            fresh = 0

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        q.append((0, r, c))
                    elif grid[r][c] == 1:
                        fresh += 1

            dist = 0

            while q:
                dist, r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((dist + 1, nr, nc))

            return dist if fresh == 0 else -1

        return bfs()