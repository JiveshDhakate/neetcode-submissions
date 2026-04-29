class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ele=float('inf')
        for i in nums:
            if i<min_ele:
                min_ele=i
        return min_ele
        