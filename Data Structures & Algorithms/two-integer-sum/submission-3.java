class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hashmap=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            int comp=target-nums[i];
            if(hashmap.containsKey(comp)){
                return  new int[] { hashmap.get(comp), i };
            }
            else{
                hashmap.put(nums[i],i);
            }
        }
        throw new IllegalArgumentException("No solution found");
    }
}
