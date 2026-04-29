class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        max_Area=0
        curr=0
        while left<=right:
            curr=(right-left)*min(heights[left],heights[right])
            max_Area=max(max_Area,curr)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_Area

            

        