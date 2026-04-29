class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        ans,max_freq=0,0
        char_freq=Counter()
        for right in range(len(s)):
            char_freq[s[right]]+=1
            max_freq=max(char_freq[s[right]],max_freq)

            while (right-left+1)-max_freq>k:
                char_freq[s[left]]-=1
                left+=1
            
            ans=max(right-left+1,ans)
        return ans
        