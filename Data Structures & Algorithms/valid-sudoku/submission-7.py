class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(i):
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False

                    seen.add(board[i][j])

            return True
        
        def check_col(j):
            seen = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            
            return True

        def check_block(r_start, c_start):
            seen = set()
            for i in range(r_start, r_start + 3):
                for j in range(c_start, c_start + 3):
                    if board[i][j] != ".":
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
            
            return True
        
        for l in range(9):
            if not check_row(l):
                return False

            if not check_col(l):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_block(i, j):
                    return False

        return True
