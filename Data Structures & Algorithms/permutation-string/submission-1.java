class Solution {
    public boolean checkInclusion(String s1, String s2) {

        if (s2.length() < s1.length()) 
            return false;

        Map<Character, Integer> s1map = new HashMap<>();

        Map<Character, Integer> s2map = new HashMap<>();

        // Building the frequency map for s1
        for (Character c : s1.toCharArray()) {
            s1map.merge(c, 1, Integer::sum);
        }

        for (int i = 0; i < s1.length(); i++) {
            s2map.merge(s2.charAt(i), 1, Integer::sum);
        }

        if (s1map.equals(s2map))
            return true;
        

        for (int i = s1.length(); i < s2.length(); i++) {
            s2map.computeIfPresent(s2.charAt(i-s1.length()), 
            (key, value) -> value == 1 ? null : value - 1);

            s2map.merge(s2.charAt(i), 1, Integer::sum);
            if (s1map.equals(s2map))
                return true;   
        }

        return false;

    }
}
