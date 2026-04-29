class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for i in strs:
            key=tuple(sorted(i))
            hashmap[key].append(i)
        result=[]    
        for value in hashmap.values():
            result.append(value)
        return result



        
        