class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1) + len(nums2)

        half = (n+1) // 2
        l, r = 0, len(nums1)

     
        while l <= r:
            mid1 = (l+r) // 2
            mid2 = half - mid1 

            leftMax1 = nums1[mid1-1] if 0< mid1 <= len(nums1) else -float('inf')
            leftMax2 = nums2[mid2-1] if 0< mid2 <= len(nums2) else -float('inf')
            rightMin1 = nums1[mid1] if 0 <= mid1 < len(nums1) else float('inf')
            rightMin2 = nums2[mid2] if 0 <= mid2 < len(nums2) else float('inf')

            if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                if n % 2 != 0:
                    return max(leftMax1, leftMax2)
                return (max(leftMax1, leftMax2) + min(rightMin1,rightMin2))/2
            elif leftMax1 > rightMin2:
                r = mid1 -1 
            else:
                l = mid1 + 1
        

