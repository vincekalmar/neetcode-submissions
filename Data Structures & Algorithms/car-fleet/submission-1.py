class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        stack = [] # time to get to target
        fleet = len(position)
        for pos, sp in sorted(zip(position, speed)):
            time = (target - pos) / sp

            while stack and time >= stack[-1]:
                stack.pop()
                fleet -= 1
            
            stack.append(time)
        
        return fleet

       # 3, 9/2, 10, 3

      #  3, 4.5

       