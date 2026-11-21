class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        indegree = [0] * numCourses
        preReq = defaultdict(set)

        for pre, course in prerequisites:
            adj[pre].add(course)
            indegree[course] += 1
    
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)


        while q: 
            pre = q.popleft()

            for course in adj[pre]:
                preReq[course].add(pre)
                preReq[course] |= preReq[pre]
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        return [pre in preReq[course] for pre, course in queries]

                
        


        
        

        

        