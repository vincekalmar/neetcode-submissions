class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def dfs(openN, closeN, s):
            if openN == closeN == n:
                res.append("".join(s))
                return

            if openN < n:
                s.append('(')
                dfs(openN + 1, closeN, s)
                s.pop()
            
            if closeN < openN:
                s.append(')')
                dfs(openN, closeN + 1, s)
                s.pop()

        dfs(0,0,[])
        return res


