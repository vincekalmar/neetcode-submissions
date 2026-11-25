class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # height, index seen
        maxArea = -1

        for i, height in enumerate(heights):
            temp = i
            while stack and stack[-1][0] > height:
                prevHeight, prevIndexSeen = stack.pop()
                maxArea = max(prevHeight * (i-prevIndexSeen), maxArea)
                temp = prevIndexSeen

            stack.append((height, temp))
        
        for height, left in stack:
            maxArea = max(maxArea, height * (len(heights) - left))

        return maxArea 