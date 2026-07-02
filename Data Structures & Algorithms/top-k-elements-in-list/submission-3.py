from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
        for num in counter:
            heappush(
                heap, (counter[num], num)
            )

            if len(heap) > k:
                heappop(heap)

        return [h[1] for h in heap]