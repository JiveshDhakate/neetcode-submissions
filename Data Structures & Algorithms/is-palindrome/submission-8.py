class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum())
        right=len(s)-1
        left=0
        while left<=right:
            if s[left].lower() != s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True

        