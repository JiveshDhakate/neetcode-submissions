class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        check_set=set()
        result=0
        for right in range(len(s)):
            while s[right] in check_set:
                check_set.remove(s[left])
                left+=1
            check_set.add(s[right])
            result=max(result,(right-left+1))
        return result
