class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0

        res = 0
        for r, c in enumerate(s):

            if c in mp:
                l = max(l, mp[c]+1)
            
            mp[c] = r
            res = max(res, r-l+1)

        return res

