class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        seen = set()

        q = deque()
        q.append((0, -1))
        seen.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                seen.add(nei)
                q.append((nei, node))

        return len(seen) == n

