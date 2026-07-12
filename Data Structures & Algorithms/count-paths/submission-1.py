class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i < 0 or j < 0 or i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            down = dp(i + 1, j)
            right = dp(i, j + 1)

            memo[(i, j)] = down + right

            return memo[(i, j)]

        return dp(0, 0)  