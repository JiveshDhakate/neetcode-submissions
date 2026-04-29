class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        hashmap_s=Counter(s)
        hashmap_t=Counter(t)
        for i in hashmap_s:
            if hashmap_s[i]!=hashmap_t[i]:
                return False
        return True
        