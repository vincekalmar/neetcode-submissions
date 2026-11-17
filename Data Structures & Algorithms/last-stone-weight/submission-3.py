class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)

        while len(maxheap) >= 2:
            
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)

            if x!=y:
                heapq.heappush(maxheap, -abs(abs(x) - abs(y)))
            
        return -heapq.heappop(maxheap) if len(maxheap) > 0 else 0
            

