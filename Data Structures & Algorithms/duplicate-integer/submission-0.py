from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashmap=Counter(nums)
         print(hashmap)
         for value in hashmap.values():
            if value>1:
                return True
         return False


         