class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=Counter(nums)
        ans=[]
        for i in hashmap.most_common(k):
            ans.append(i[0])
        return ans




        
            
            
        