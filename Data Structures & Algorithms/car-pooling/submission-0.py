class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda arr : arr[1])
        
        minheap = []
        heapq.heapify(minheap)
        car = 0

        for people, start, end in trips:

            while minheap and minheap[0][0] <= start:
                car -= heapq.heappop(minheap)[1]
            car += people
            if car > capacity:
                return False

            heapq.heappush(minheap, (end, people))

        return True

