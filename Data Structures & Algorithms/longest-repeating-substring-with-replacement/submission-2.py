class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        l = 0
        res = 0
        
        mostFrequent = 0
        for r, c in enumerate(s):
            count[c] += 1
            mostFrequent = max(mostFrequent, count[c])

            while (r-l + 1) - mostFrequent > k:
                count[s[l]] -= 1
                l +=1 
            
            res = max(r-l+1, res)
            
        return res 
