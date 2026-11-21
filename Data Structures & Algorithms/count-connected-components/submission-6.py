class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()
        count = 0
        
        for i in range(n):
            if i not in seen:
                q = deque()
                q.append(i)
                seen.add(i)

                while q:
                    node = q.popleft()

                    for nei in adj[node]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei) 
                count += 1
        
        return count
