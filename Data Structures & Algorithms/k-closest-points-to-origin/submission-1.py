from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point
            dist = x ** 2 + y ** 2 
            heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heappop(heap)
        res = []

        for dist, x , y in heap:
            res.append([x, y])

        return res