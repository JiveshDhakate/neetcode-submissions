from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkset=set()
        for i in nums:
            if i in checkset:
                return True
            else:
                checkset.add(i)
        return False


         