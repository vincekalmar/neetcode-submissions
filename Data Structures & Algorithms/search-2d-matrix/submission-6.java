class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
    
        int up = 0, down = matrix.length - 1;
        int row = 0;
        while (up <= down) {
            row = (up + down) / 2;

            if (matrix[row][matrix[row].length - 1] > target) {
                down = row - 1;
            }
            else if (matrix[row][matrix[row].length - 1] < target) {
                up = row + 1;
            }
            else {
                return true;
            }

        }
        row = up;
        if (row == matrix.length) return false;
        
        int l = 0, r = matrix[row].length - 1;

        while (l <= r) {
            int mid = (l + r) / 2;

            if (matrix[row][mid] > target) {
                r = mid - 1;
            }
            else if (matrix[row][mid] < target) {
                l = mid + 1;
            }
            else {
                return true;
            }
        }

        return false;

    }
}
