class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        int[] arr = new int [26];
        int bound = (int)'z';
        for (int i = 0; i < s.length(); i++) {
            arr[(int)(bound - s.charAt(i))]++;
            arr[(int)(bound - t.charAt(i))]--;
        }

        for (int c : arr) {
            if (c != 0)
                return false;
        }
        return true;
    }

}