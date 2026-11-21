class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        degree = [0] * (len(edges) + 1)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque()
        for i in range(len(edges)):
            if degree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()

            for nei in adj[node]:
                degree[nei] -= 1
                if degree[nei] == 1:
                    q.append(nei)


        for u, v in reversed(edges):
            if degree[u] >= 2 and degree[v] >= 2:
                return [u,v]

        return [1,2]
                