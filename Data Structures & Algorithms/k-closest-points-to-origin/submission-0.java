class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Queue<double[]> pq = new PriorityQueue<>((a,b) -> Double.compare(b[0], a[0]));

        for (int[] point: points) {
            int x = point[0];
            int y = point[1];
            double distance = Math.sqrt(Math.pow(x,2) + Math.pow(y,2));

            if (pq.size() < k) pq.offer(new double[]{distance, x, y});
            else {
                if (distance < pq.peek()[0]) {
                    pq.poll();
                    pq.offer(new double[]{distance, x, y});
                }
            }
        }

        List<int[]> res = new ArrayList<>();

        for (double[] triple : pq) {
            res.add(new int[]{(int)triple[1], (int)triple[2]});
        }

        return res.toArray(new int[res.size()][]);

    }


}
