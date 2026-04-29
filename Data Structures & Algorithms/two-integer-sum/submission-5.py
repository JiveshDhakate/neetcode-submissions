class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for i,num in enumerate(nums):
            val=target-num
            if val in nums_map:
                return [nums_map[val],i]
            nums_map[num]=i