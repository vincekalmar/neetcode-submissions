class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[course].append(prereq)
            indegree[prereq] += 1
        
        q = deque()

        for course, degree in enumerate(indegree):
            if degree == 0:
                q.append(course)
        finish = 0
        while q:
            course = q.popleft()
            finish += 1
            for prereq in adj[course]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)

        return finish == numCourses



      