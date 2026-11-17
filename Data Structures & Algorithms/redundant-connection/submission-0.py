class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)
        

        def find(node):
            par = parent[node]
            while par != node:
                par = parent[par]
                node = parent[node]
            return par


        def union(u,v):
            parent1, parent2 = find(u), find(v)


            if parent1 == parent2:
                return True
            
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
            
            else:
                parent[parent1] = parent2
                rank[parent2] += 1
                
            return False

        for u, v in edges:
            if union(u,v):
                return [u,v]