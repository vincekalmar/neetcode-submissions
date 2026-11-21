class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
       
        if len(edges) != n - 1:
            return False
        adj = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

    
    

        q = deque()
        for i in range(n):
            if degree[i] == 1:
                degree[i] -= 1
                q.append(i)
        
        while q:

            node = q.popleft()

            for nei in adj[node]:
                degree[nei] -= 1
                if degree[nei] == 1:
                    q.append(nei)


        for i in range(n):
            if degree[i] >= 2:
                return False
        return True
                






    