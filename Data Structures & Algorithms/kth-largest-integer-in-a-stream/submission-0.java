class KthLargest {

    private int k;
    Queue<Integer> pq;
    
    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.pq = new PriorityQueue<>();
        for (int num : nums) {
            if(this.pq.isEmpty() || this.pq.size() < this.k)
                this.pq.offer(num);
            else if (num > this.pq.peek()) {
                this.pq.poll();
                this.pq.offer(num);
            }
        }
    }
    
    public int add(int val) {

        if(this.pq.isEmpty() || this.pq.size() < k)
                this.pq.offer(val);
            else if (val > this.pq.peek()) {
                this.pq.poll();
                this.pq.offer(val);
            }
        return this.pq.peek();
    }
}
