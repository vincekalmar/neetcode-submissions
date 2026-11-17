class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [[] for _ in range(n+1)]

        for u, v, t, in times:
            adj[u].append((v,t))
        
        minheap = [(0,k)]
        heapq.heapify(minheap)
        explored = set()


        while minheap:

            time, node = heapq.heappop(minheap)
            if node in explored:
                continue

            explored.add(node)
        
            if len(explored) == n:
                return time
                

            for nei, t in adj[node]:
                if nei in explored:
                    continue
                heapq.heappush(minheap, (time + t, nei))
        
        return -1
