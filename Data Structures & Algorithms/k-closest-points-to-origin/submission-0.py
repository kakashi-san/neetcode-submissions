from heapq import heappush, heappop
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x, y):
            return math.sqrt(x**2 + y**2)

        heap = []
        
        for point in points:
            x, y = point
            distXY = dist(x, y)

            heappush(heap, (- dist(x, y), (x,y)))

            if len(heap) > k:
                heappop(heap)

        return [point for _, point in heap]