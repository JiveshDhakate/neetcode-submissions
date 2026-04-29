class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for idx,value in enumerate(nums):
            comp=target-value
            if comp in num_map:
                return [num_map[comp],idx]
            else:
                num_map[value]=idx
        return -1       