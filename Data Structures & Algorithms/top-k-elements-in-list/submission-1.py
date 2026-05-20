from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        heap = []

        for num in counter:
            heappush(heap, (counter[num], num))

            if len(heap) > k:
                heappop(heap)
        res = [hi[1] for hi in heap]

        return res
        