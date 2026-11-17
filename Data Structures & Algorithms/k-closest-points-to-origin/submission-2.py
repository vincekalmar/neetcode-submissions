class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxheap = []
        heapq.heapify(maxheap)


        for x,y in points:
            distance = -math.sqrt(x**2 + y**2)

            if len(maxheap) < k:
                heapq.heappush(maxheap,(distance, x,y))
            elif distance > maxheap[0][0]:
                heapq.heappop(maxheap)
                heapq.heappush(maxheap,(distance, x,y))


        res = []

        while maxheap:
            _,x,y = heapq.heappop(maxheap)            
            res.append([x,y])
        return res

