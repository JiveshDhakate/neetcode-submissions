class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashs={}
        hasht={}
        for i in range(len(s)):
            hashs[s[i]]=hashs.get(s[i],0)+1
            hasht[t[i]]=hasht.get(t[i],0)+1
        for key in hashs:
            if key not in hasht or hashs[key]!=hasht[key]:
                return False
        return True

        
        
        