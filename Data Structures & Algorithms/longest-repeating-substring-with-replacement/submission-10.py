class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        count = defaultdict(int)

        maxFreqChar = 0

        l = 0

        res = 0
        for r, c in enumerate(s):
            
            count[c] += 1
            
            maxFreqChar = max(maxFreqChar, count[c])
            
            while (r-l+1) - maxFreqChar > k:
                count[s[l]] -= 1
                l+=1
            
            res = max(res, r-l+1)


            
        return res
            