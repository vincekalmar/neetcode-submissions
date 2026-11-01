class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = Arrays.stream(piles).max().getAsInt();
        int min_rate = Integer.MAX_VALUE;

        while (l <= r) {   
            int mid = l + (r-l) / 2;

            if (timeForBannanas(mid, piles) <= h) {
                min_rate = Math.min(min_rate, mid);
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }
        return min_rate;
    }

    public long timeForBannanas(int rate, int[] piles) {
        long res = 0;
        for (int i = 0; i < piles.length; i++) {
            res += ((long)piles[i] + rate - 1) / rate;
        }
        return res;
    }
}
