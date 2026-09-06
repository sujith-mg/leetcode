class Solution {
    public void rotate(int[] nums, int k) {
        k=k%nums.length;
        r(nums,0,nums.length-1);
        r(nums,0,k-1);
        r(nums,k,nums.length-1);

        
    }
    public void r(int[] nums,int left,int right){
        while(left<right){
            int temp=nums[left];
            nums[left]=nums[right];
            nums[right]=temp;
            left++;
            right--;
        }
    }
}