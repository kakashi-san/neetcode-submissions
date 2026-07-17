class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        zeros = []

        for r in range(ROWS):
            for c in range(COLS):
                 if matrix[r][c] == 0:
                    zeros.append((r,c))

        def row_zerod(r):
            for c in range(COLS):
                matrix[r][c] = 0 

        def col_zerod(c):
            for r in range(ROWS):
                matrix[r][c] = 0 

        for (r,c) in zeros:
            row_zerod(r)
            col_zerod(c)