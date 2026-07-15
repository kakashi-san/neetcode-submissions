class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if r < c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        def flip_row(r):
            for i in range(COLS // 2):
                matrix[r][i],  matrix[r][COLS - i - 1] = matrix[r][COLS - i - 1], matrix[r][i]

        
        for r in range(ROWS):
            flip_row(r)

        
