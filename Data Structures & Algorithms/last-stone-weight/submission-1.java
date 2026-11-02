class Solution {
    public int lastStoneWeight(int[] stones) {
        if (stones.length == 0) return 0;

        Queue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        pq.addAll(Arrays.stream(stones).boxed().toList());


        while (pq.size() > 1) {
            int prevStone = pq.poll(); //6
            int currStone = pq.poll(); // 4
            int newStone = Math.abs(currStone - prevStone); // 6-4 = 2

            if (newStone != 0) {
                pq.offer(newStone); // 2
            }
        }
        return pq.isEmpty() ? 0 : pq.poll();
    }
}
