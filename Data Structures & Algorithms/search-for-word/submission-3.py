class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        def rec(i, bi, bj):
            if i == len(word):
                return True

            if bi < 0 or bi >= ROWS or bj < 0 or bj >= COLS:
                return False

            if word[i] == board[bi][bj]:
                temp = board[bi][bj]
                board[bi][bj] = "#"
                found = (
                    rec(i + 1, bi + 1, bj)
                    or rec(i + 1, bi , bj + 1)
                    or rec(i + 1, bi - 1, bj)
                    or rec(i + 1, bi , bj - 1)
                    )
                board[bi][bj] = temp
                return found
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if rec(0, r, c):
                    return True

        return False