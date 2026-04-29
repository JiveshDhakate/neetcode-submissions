class Solution {
    public int maxArea(int[] heights) {
        int l=0;
        int r=heights.length-1;
        int max_Area=0;
        while(l<=r){
            int curr=(r-l)*Math.min(heights[l],heights[r]);
            max_Area=Math.max(curr,max_Area);
            if(heights[l]<heights[r]){
                l++;
            }
            else {
                r--;
            }
        }
        return max_Area;
        
    }
}
