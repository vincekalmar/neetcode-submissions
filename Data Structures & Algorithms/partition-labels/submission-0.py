class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastIndex = {}

        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        start = end = 0
        res = []
        for i, c in enumerate(s):

            end = max(lastIndex[c], end)
            if i == end:
                res.append(end-start+1)
                start = end + 1
        return res
