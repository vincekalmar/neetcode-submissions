class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<List<Integer>, List<String>> freq = new HashMap<>();

        for (String str : strs) {
            int[] char_count = new int[26];

            for (char c : str.toCharArray()) {
                char_count[c - 'a']++;
            }

            List<Integer> key = Arrays.stream(char_count)
                                      .boxed()
                                      .toList();

            freq.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }

        List<List<String>> res = new ArrayList<>();

        freq.forEach((key, value) -> {
            res.add(value);
        });

        return res;
    }
}