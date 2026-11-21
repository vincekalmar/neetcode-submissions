class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            pre = q.popleft()

            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        for i in range(numCourses):
            if indegree[i]: return False

        return True
                

        