class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list={}
        for i in range(n):
            adj_list[i]=[]

        for source,destination in edges:
            adj_list[source].append(destination)
            adj_list[destination].append(source)
        
        
        def dfs(vertex,path,visited):
            visited.add(vertex)
            path.append(vertex)
            for neigh in adj_list[vertex]:
                if neigh not in visited:
                    dfs(neigh,path,visited)
            return path

        paths=[]
        visited=set()
        for i in range(n):
            if i not in visited:
                curr_path=dfs(i,[],visited)
                paths.append(curr_path)
        return len(paths)
        