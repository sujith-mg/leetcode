class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right=height.length-1;
        int max_area=0;
        while(left<right){
            int width=right-left;
            int h = Math.min(height[left], height[right]);
            int area=h * width;
            max_area=Math.max(max_area,area);
            if(height[left]<height[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return max_area;
        
    }
}