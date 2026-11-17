class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.minheap = []
        heapq.heapify(self.minheap)
        self.k = k
        for num in nums:
            if len(self.minheap) < self.k:
                heapq.heappush(self.minheap, num)

            elif num > self.minheap[0]:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, num)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
                heapq.heappush(self.minheap, val)
        elif val > self.minheap[0]:
            heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val)
        return self.minheap[0]
        
