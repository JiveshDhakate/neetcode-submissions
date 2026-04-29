class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < numbers.length; i++) {
            int comp = target - numbers[i];
            if (hashMap.containsKey(comp)) {
                return new int[]{hashMap.get(comp) + 1, i + 1};
            }
            hashMap.put(numbers[i], i);
        }
        return new int[] {};
        
    }
}
