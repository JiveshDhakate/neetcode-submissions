class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list={i:[] for i in range(n)}
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited=set()
        def dfs(source,parent):
            visited.add(source)
            for neigh in adj_list[source]:
                if neigh in visited and neigh!=parent:
                    return False
                if neigh not in visited:
                    if dfs(neigh,source)==False:
                        return False
            return True
        if dfs(0,-1)==False:
            return False
        return len(visited)==n

            
            
        