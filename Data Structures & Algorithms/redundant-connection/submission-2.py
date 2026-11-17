class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(len(edges) + 1)]
        degree = [0] * (len(edges) +1)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque()

        for i in range(1,len(edges)+1):
            if degree[i] == 1:
                q.append(i)

   #     2, 5
   #     5, 1

     #   1, 4

        while q:
            node = q.popleft()
            degree[node] -= 1
            for nei in adj[node]:
                degree[nei] -= 1
                if degree[nei] == 1:
                    q.append(nei)
            
        for u,v in reversed(edges):
            if degree[u] >= 2 and degree[v] >= 2:
                return [u,v]





