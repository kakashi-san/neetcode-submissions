class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time(k):
            t = 0
            for b in piles:
                t += math.ceil(b / k)
            return t

        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            time = get_time(mid)
            if time > h:
                l = mid + 1
            else:
                r = mid

        return r