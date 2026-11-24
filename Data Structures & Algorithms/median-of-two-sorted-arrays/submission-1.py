class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1) + len(nums2)

        l1, r1 = 0, len(nums1)

        half = (n+1) // 2

        while l1 <= r1:
            mid1 = (l1 + r1) // 2
            mid2 = half - mid1

            maxLeft1 = nums1[mid1-1] if mid1 - 1 >= 0 else -float('inf')
            maxLeft2 = nums2[mid2-1] if mid2 - 1 >= 0 else -float('inf')
            minRight1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
            minRight2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if n % 2 != 0:
                    return max(maxLeft1, maxLeft2)
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2

            elif maxLeft1 > minRight2:
                r1 = mid1 - 1
            elif maxLeft2 > minRight1:
                l1 = mid1 + 1




