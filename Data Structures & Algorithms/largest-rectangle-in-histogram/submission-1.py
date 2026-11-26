class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        heights.append(0)
        for r, height in enumerate(heights):
            start = r

            while stack and height < stack[-1][0]:
                prevHeight, l = stack.pop()

                area = prevHeight * (r-l)
                maxArea = max(maxArea, area)
                start = l

            stack.append((height, start))


        return maxArea
