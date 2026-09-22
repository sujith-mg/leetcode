class Solution {
    public int[] twoSum(int[] nums, int target) {
       HashMap<Integer,Integer> prevmap=new HashMap<>();
        for (int i=0;i<nums.length;i++){
             int diff=target-nums[i];
            if(prevmap.containsKey(diff)){
                return new int[]{prevmap.get(diff),i};
                           
        }
         prevmap.put(nums[i],i);  
       
        
    }
     return new int[]{};
}
}