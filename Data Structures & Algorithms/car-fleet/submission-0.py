class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        cars = list(zip(position, speed))
        cars.sort()

        stack = []
        fleet = 0
        for p, s in cars:
            time = (target-p)/s
            # while the time is greater than equal to last car
            while stack and time >= stack[-1]: 
                stack.pop()
                fleet += 1

            stack.append(time)

        return len(stack)


      #  1 4, target = 10
      #  3 2

      #  (target - pos) / speeed >= (target - p) / speed
      #  6 / 2 = 3
     #   9 / 3 = 3