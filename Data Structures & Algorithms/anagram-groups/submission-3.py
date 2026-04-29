class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_map=defaultdict(list)
        for i in strs:
            grp_map[tuple(sorted(i))].append(i)
        return list(grp_map.values())