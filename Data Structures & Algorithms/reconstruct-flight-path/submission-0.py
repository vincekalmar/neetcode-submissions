class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)


        res = []
        stack = ['JFK']

        while stack:
            current = stack[-1]
            if not adj[current]:
                res.append(stack.pop())
            else:
                stack.append(adj[current].pop())
         

        return list(reversed(res))


