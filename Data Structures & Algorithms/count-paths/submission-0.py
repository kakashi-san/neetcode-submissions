class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def countPaths(i, j):
            if i >= m or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m - 1 and j == n - 1:
                return 1
            
            memo[(i, j)] = countPaths(i + 1, j) + countPaths(i, j + 1)

            return memo[(i, j)]

        return countPaths(0, 0)