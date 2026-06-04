from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        heap = []

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, count in counter.items():
            heappush(heap, (count, num))
            if len(heap) > k:
                heappop(heap)

        return [num for count, num in heap]