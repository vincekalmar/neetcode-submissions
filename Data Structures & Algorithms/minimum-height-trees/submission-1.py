class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
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
                q.append(i)

        remaining = n

        while remaining > 2:
            n = len(q)
            remaining -= n
            for _ in range(n):
                node = q.popleft()

                for nei in adj[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)
        

        