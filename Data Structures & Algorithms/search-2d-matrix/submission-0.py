class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        u, d = 0, ROWS - 1
        l, r = 0, COLS - 1


        while u <= d:
            midR = (u + d) // 2
            if target < matrix[midR][0]:
                d = midR - 1
            elif target > matrix[midR][COLS - 1]:
                u = midR + 1
            
            else:
                while l <= r:
                    midC =  (l + r) // 2
                    if target == matrix[midR][midC]:
                        return True
                    elif target > matrix[midR][midC]:
                        l = midC + 1

                    else:
                        r = midC - 1

                return False
        
        return False