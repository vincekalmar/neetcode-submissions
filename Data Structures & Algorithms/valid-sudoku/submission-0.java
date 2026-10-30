class Solution {
    public boolean isValidSudoku(char[][] board) {

        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> boxes = new HashMap<>();

        for (int row = 0; row < 9; row++) {

            Set<Character> rowSet = new HashSet<>();

            for (int col = 0; col < 9; col++) {

                char num = board[row][col];

                if (num == '.') {
                    continue;
                }

                int box = (row / 3) * 3 + (col / 3);

                cols.putIfAbsent(col, new HashSet<>());
                boxes.putIfAbsent(box, new HashSet<>());

                if (!rowSet.add(num) ||
                    !cols.get(col).add(num) ||
                    !boxes.get(box).add(num)) {

                    return false;
                }
            }
        }

        return true;
    }
}