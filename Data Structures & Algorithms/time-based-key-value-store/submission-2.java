class TimeMap {
    private Map<String, TreeMap<Integer, String>> mp;

    public TimeMap() {
        mp = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        mp.computeIfAbsent(key, k -> new TreeMap<>()).putIfAbsent(timestamp, value);
    }
    
    public String get(String key, int timestamp) {
        if (!mp.containsKey(key)) return "";
        Map.Entry<Integer, String> entry = mp.get(key).floorEntry(timestamp);

        if (entry == null)
            return "";
        return entry.getValue();
    }
}
