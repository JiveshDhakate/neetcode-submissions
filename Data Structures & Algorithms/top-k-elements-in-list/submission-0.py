class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h1=Counter(nums)
        most_common = h1.most_common(k) 
        ans=[]
        for key,value in most_common:
            ans.append(key)
        return ans



        
            
            
        