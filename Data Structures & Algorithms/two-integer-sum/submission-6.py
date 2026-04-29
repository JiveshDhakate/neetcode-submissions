class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for idx,num in enumerate(nums):
            val=target-num
            if val in nums_map:
                return [nums_map[val],idx]
            nums_map[num]=idx