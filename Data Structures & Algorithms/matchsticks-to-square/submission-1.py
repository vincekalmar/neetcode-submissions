class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        
        total = sum(matchsticks)
        if total % 4 != 0: return False


        sides = [0] * 4
        targetSide = total // 4
        matchsticks.sort(reverse=True)

        def dfs(current):
            if current == len(matchsticks):
                return True
            

            for i in range(4):
                if matchsticks[current] + sides[i] <= targetSide:
                    sides[i] += matchsticks[current]

                    if dfs(current+1):
                        return True
                    sides[i] -= matchsticks[current]

                if sides[i] == 0:
                    break
            
            return False
        
        return dfs(0)
                



