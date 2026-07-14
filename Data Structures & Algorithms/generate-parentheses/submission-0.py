class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def rec(curr_str, n_open, n_close):
            if len(curr_str) == 2*n:
                res.append(curr_str)
                return 
            
            if n_open < n:
                rec(curr_str + "(", n_open + 1 , n_close)

            if n_close < n_open:  
                rec(curr_str + ")", n_open , n_close + 1)

        rec("", 0, 0)
        return res