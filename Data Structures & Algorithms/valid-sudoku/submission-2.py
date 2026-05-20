class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)

        def check_row(i) -> bool:
            seen = set()
            for c in range(N):
                if board[i][c] != "." and board[i][c] in seen:
                    return False
    
                if board[i][c] != ".":
                    seen.add(board[i][c])
            
            return True

        def check_col(i) -> bool:
            seen = set()
            for r in range(N):
                if board[r][i] != "." and board[r][i] in seen:
                    return False
    
                if board[r][i] != ".":
                    seen.add(board[r][i])
            
            return True
        
        def check_grid(i, j) -> bool:
            seen = set()

            for r in range(i, i + 3):
                for c in range(j, j + 3):
    
                    if board[r][c] != "." and board[r][c] in seen:
                        return False
    
                    if board[r][c] != ".":
                        seen.add(board[r][c])

            return True

        for r in range(N):
            if check_row(r) is False:
                return False
        for c in range(N):
            if check_col(c) is False:
                return False
        
        grid_starts = [
            (0, 0), (0, 3), (0 ,6),
            (3, 0), (3, 3), (3 ,6),
            (6, 0), (6, 3), (6 ,6),
        ]
        for grid_start in grid_starts:
            if check_grid(*grid_start) is False:
                return False
        
        return True







