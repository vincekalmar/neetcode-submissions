class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = deque()

        q.append((beginWord,1))
        seen = set()

        wordList = set(wordList)

        res = 'abcdefghijklmnopqrstuvwxyz'

        while q:

            word, distance = q.popleft()

            for i, c in enumerate(word):

                for letter in res:
                    nei = word[:i] + letter + word[i+1:]

                    if nei in wordList and nei not in seen:
                        q.append((nei, distance + 1))
                        seen.add(nei)

                        if nei == endWord:
                            return distance + 1
                    



        return 0





    
   