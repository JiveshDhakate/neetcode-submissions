class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        forward=1
        for i in range(len(nums)):
            result[i]=forward
            forward*=nums[i]
        backward=1
        for j in range(len(nums)-1,-1,-1):
            result[j]*=backward
            backward*=nums[j]
        return result
        # res=[]
        # for i in range(len(nums)):
        #     mul=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             mul*=nums[j]
        #     res.append(mul)
        # return res



        