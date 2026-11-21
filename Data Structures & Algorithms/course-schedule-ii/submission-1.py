class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)

        res = []
        while q:

            pre = q.popleft()
            res.append(pre)

            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        return res if len(res) == numCourses else []

        
        