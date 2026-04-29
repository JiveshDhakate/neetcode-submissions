class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined_s=''
        for i in s:
            if i.isalnum():
                joined_s+=i.lower()
        left=0
        right=len(joined_s)-1
        while left<right:
            if joined_s[left]!=joined_s[right]:
                return False
            left+=1
            right-=1
        return True

        