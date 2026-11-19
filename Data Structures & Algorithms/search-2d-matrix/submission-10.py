class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        l,r = 0, ROW -1 
        arr = []
        while l <= r:

            mid = (l+r) // 2

            if target < matrix[mid][0]:
                r= mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                arr = matrix[mid]
                break

        l, r = 0, COL - 1
        if not arr:
            return False

        while l <= r:

            mid = (l+r) // 2

            if target < arr[mid]:
                r = mid - 1
            elif target > arr[mid]:
                l = mid + 1
            else:
                return True
        
        return False


        

        