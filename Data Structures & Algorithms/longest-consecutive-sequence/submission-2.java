class Solution {
    public int longestConsecutive(int[] nums) {

        Map<Integer, Integer> mp = new HashMap<>();

        int max = 0;

        for (int i = 0; i < nums.length; i++) {

            int num = nums[i];

            // Skip duplicates
            if (mp.containsKey(num)) {
                continue;
            }

            // Get lengths of neighboring sequences
            int left = mp.getOrDefault(num - 1, 0);
            int right = mp.getOrDefault(num + 1, 0);

            // Calculate merged sequence length
            int length = left + right + 1;

            // Find boundaries
            int lookback = num - left;
            int lookahead = num + right;

            // Store current number
            mp.put(num, length);

            // Update both boundaries
            mp.put(lookback, length);
            mp.put(lookahead, length);

            // Update maximum
            max = Math.max(max, length);
        }

        return max;
    }
}