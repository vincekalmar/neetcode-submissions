class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> freq = new HashMap<>();

        PriorityQueue<Integer[]> pq = new PriorityQueue<>((a,b) -> Integer.compare(a[1], b[1]));

        for (Integer num : nums) {
            freq.merge(num, 1, Integer::sum);
        }

        freq.forEach((key, val) -> {
            Integer[] tup = {key, val};

            if (pq.size() < k)
                pq.add(tup);
            else {
                if(tup[1] > pq.peek()[1]) {
                    pq.poll();
                    pq.add(tup);
                }
            }
        });
        int[] res = new int[k];
        int i = 0;

        while (!pq.isEmpty()) {
            res[i] = pq.poll()[0];
            i++;    
        }
        return res;


    }
}
