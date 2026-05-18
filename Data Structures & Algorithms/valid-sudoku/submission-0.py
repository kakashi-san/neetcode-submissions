from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board)
        
        def check_row(i):
            seen_nums = set()
            for c in range(COLS):
                if board[i][c] != "." and board[i][c] in seen_nums:
                    return False
                seen_nums.add(board[i][c])
            return True
        
        def check_col(j):
            seen_nums = set()
            for r in range(ROWS):
                if board[r][j] != "." and board[r][j] in seen_nums:
                    return False
                seen_nums.add(board[r][j])
            return True
        
        def check_block(i, j):
            seen_nums = set()
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    if board[r][c] != "." and board[r][c] in seen_nums:
                        return False
                    seen_nums.add(board[r][c])
            return True
        
        for r in range(ROWS):
            if not check_row(r):
                return False
        
        for c in range(COLS):
            if not check_col(c):
                return False
        
        for (r, c) in [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]:
            if not check_block(r, c):
                return False
        
        return True