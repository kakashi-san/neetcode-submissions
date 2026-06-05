class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board)

        def check_row(i):
            seen_ = set()
            j = 0
            while j < COLS:
                if board[i][j] != '.' and board[i][j] in seen_:
                    return False
                elif board[i][j] != '.':
                    seen_.add(board[i][j])
                j += 1
            return True

        def check_col(j):
            seen_ = set()
            i = 0
            while i < ROWS:
                if board[i][j] != '.' and board[i][j] in seen_:
                    return False
                elif board[i][j] != '.':
                    seen_.add(board[i][j])
                i += 1
            return True

        def check_grid(i, j):
            seen_ = set()
            for x in range(i + 3):
                for y in range(j + 3):
                    if board[x][y] != '.' and board[x][y] in seen_:
                        return False
                    elif board[x][y] != '.':
                        seen_.add(board[x][y])
            return True

        def check_grid(i, j):
            seen_ = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if board[x][y] != '.' and board[x][y] in seen_:
                        return False
                    elif board[x][y] != '.':
                        seen_.add(board[x][y])
            return True

        for i in range(ROWS):
            if not check_row(i):
                return False

        for j in range(COLS):
            if not check_col(j):
                return False

        
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                if not check_grid(x, y):
                    return False

        return True
