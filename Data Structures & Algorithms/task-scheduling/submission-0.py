class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        
        maxheap = [[-c, 0] for c in count.values()]
        heapq.heapify(maxheap)

        elapsedTime = 0
        cooldown = deque()
        while maxheap or cooldown:
            elapsedTime += 1

            if maxheap:
                remaining, time = heapq.heappop(maxheap)
                remaining += 1
                if remaining < 0:
                    cooldown.append([remaining, elapsedTime + n])


            
            if cooldown and cooldown[0][1] <= elapsedTime:
                heapq.heappush(maxheap, cooldown.popleft())
        
        return elapsedTime

        
            
