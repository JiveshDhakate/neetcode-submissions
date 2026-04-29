class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h1=defaultdict(list)
        for i in strs:
            key=tuple(sorted(i))
            if i in h1:
                h1[key].append(i)
            h1[key].append(i)
        return h1.values()
        