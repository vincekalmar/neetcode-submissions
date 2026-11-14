class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for string in strs:

            hash = [0] * 26

            for c in string:
                hash[ord(c) - ord('a')] +=1

            mp[tuple(hash)].append(string) 
        
        return list(mp.values())


