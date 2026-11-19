class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        leftHeight = rightHeight = 0

        water = 0
        while l <= r:

            leftHeight = max(leftHeight, height[l])
            rightHeight = max(rightHeight, height[r])

            if leftHeight <= rightHeight:
                depth = leftHeight - height[l]
                if depth > 0:
                    water += depth
                l+=1
            else:
                depth = rightHeight - height[r]
                if depth > 0:
                    water += depth
                r-=1
        return water


