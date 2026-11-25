class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        shortestJobs = []
        heapq.heapify(shortestJobs)
        waitingJobs = deque(sorted([task[0], task[1], i] for i, task in enumerate(tasks)))
       
        res = []
        elapsedTime = 0

        while shortestJobs or waitingJobs:
            if not shortestJobs:
                elapsedTime = max(elapsedTime, waitingJobs[0][0])
            
            while waitingJobs and waitingJobs[0][0] <= elapsedTime:
                sTime, pTime, i = waitingJobs.popleft()
                heapq.heappush(shortestJobs, (pTime, sTime, i))

            
            pTime, sTime, job = heapq.heappop(shortestJobs)
            res.append(job)
            elapsedTime += pTime
            


        return res





            

