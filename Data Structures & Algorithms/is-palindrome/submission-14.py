class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_s=''
        for i in s:
            if i.isalnum():
                check_s+=i.lower()
        l,r=0,len(check_s)-1
        while l<r:
            if check_s[l]!=check_s[r]:
                return False
            l+=1
            r-=1
        return True

        