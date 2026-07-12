class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            if n == 0:
                return 1

            if n % 2 == 1:
                a = pow(x, n // 2)
                return a * a * x
            
            else:
                a = pow(x, n // 2)
                return a * a

        if n < 0:
            x = 1 / x
            n = -n
            
        return pow(x, n)