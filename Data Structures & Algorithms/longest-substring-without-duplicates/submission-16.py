class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        l,r=0,0
        check_set=set()
        max_len,substr=0,''
        while r!=len(s):
            if s[r] not in check_set:
                check_set.add(s[r])
                r+=1
            else:
                max_len=max(len(check_set),max_len)
                l+=1
                r=l
                check_set.clear()
        max_len=max(len(check_set),max_len)
        return max_len
        