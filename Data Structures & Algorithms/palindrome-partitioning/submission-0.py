class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(t):
            l, r = 0, len(t) - 1
            while l < r:
                if t[l] != t[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        res = []
        def dfs(start, partition):
            if start == len(s):
                res.append(partition.copy())
                return


            for current in range(start, len(s)):
                temp = s[start:current+1]
                if not isPali(temp):
                    continue
                partition.append(temp)
                dfs(current+1, partition)
                partition.pop()

        dfs(0, [])
        return res

            
        


