class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        adj = defaultdict(list)

        for edge, value in zip(equations, values):
            u = edge[0]
            v = edge[1]
            adj[u].append((v, value))
            adj[v].append((u, 1/value))

        print(adj)
        
        res = []

        for num, den in queries:
                
            q = deque()
            seen = set()
            seen.add(num)
            q.append((num, 1))
            found = False

            if num in adj and num == den:
                print("h")
                found = True
                res.append(1)
            if num not in adj or den not in adj:
                found = True
                res.append(-1)
            while q and not found:
                curr, value = q.popleft()

                for nei, v in adj[curr]:
                    if nei not in seen:
                        if  nei == den:
                            res.append(value * v)
                            found = True
                            break
                        q.append((nei, value * v))
                        seen.add(nei)
            if not found:
                res.append(-1)

        return res








