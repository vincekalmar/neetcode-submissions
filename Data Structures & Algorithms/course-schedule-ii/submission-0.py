class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses


        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        q = deque()

        for prereq, degree in enumerate(indegree):
            if degree == 0:
                q.append(prereq)

        res = []

        while q:

            prereq = q.popleft()

            res.append(prereq)

            for course in adj[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return res if len(res) == numCourses else []


