class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def dfs(i, sub):
            if len(sub) == k:
                res.append(sub.copy())
                return
            if i > n:
                return

            sub.append(i)
            dfs(i+1, sub)
            sub.pop()
            dfs(i+1, sub)

        dfs(1,[])
        return res
