class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        
        for arr in adj:
            if not arr:
                n-=1
                


        print(adj)

        count = len(adj) - n
        for u, v in edges:

            if u not in seen and v not in seen:
                q = deque()
                q.append(u)
                seen.add(u)
                while q:
                    node = q.popleft()

                    for nei in adj[node]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)

                count += 1
        
        return count

       
