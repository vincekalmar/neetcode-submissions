class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))

        minheap = []
        minheap.append((0,k))
        heapq.heapify(minheap)
        seen = {}
        seen[k] = 0

        while minheap:
            print(seen)
            time, node = heapq.heappop(minheap)
            for x, t in adj[node]:
                if x not in seen or time + t < seen[x]:
                    seen[x] = time+t
                    heapq.heappush(minheap,((time+t, x)))

        if len(seen) == n:
            maxTime = 0
            for k, v in seen.items():
                maxTime = max(v, maxTime)
            return maxTime


        return -1


