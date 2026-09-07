class Solution {
    public int majorityElement(int[] nums) {
          int num=0;
        int counts=0;  
   for( int i=0;i<nums.length;i++){
    if(counts==0){
        num=nums[i];
        counts++;
    }
    else if(num==nums[i]){
        counts++;
    }
    else{
        counts--;
    }
   }
   return num;
    }
}