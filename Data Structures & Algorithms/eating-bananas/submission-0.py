import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1

        def eat_time(piles, k):
            t = 0
            for pile in piles:
                t += math.ceil(pile / k)
            return t


        while max_k > min_k:
            mid_k = (max_k + min_k) // 2
            t = eat_time(piles, mid_k)

            if t > h:
                min_k = mid_k + 1
            
            else:
                max_k = mid_k

        return max_k




