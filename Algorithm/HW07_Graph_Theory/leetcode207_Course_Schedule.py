# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/

# Runtime: 40 ms
# Memory Usage: 14.2 MB
# Your runtime beats 97.05 % of python3 submissions.
# Your memory usage beats 86.34 % of python3 submissions.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        edges = {i:[] for i in range(numCourses)}
        for order in prerequisites:
            indegree[order[0]] += 1
            edges[order[1]] += [order[0]]
        
        
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        coursetaken = 0
        while queue:
            course = queue.popleft()
            coursetaken += 1
            for i in edges[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return coursetaken == numCourses