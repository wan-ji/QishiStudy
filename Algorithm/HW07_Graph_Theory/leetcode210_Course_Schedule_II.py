# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/description/

# Runtime: 48 ms
# Memory Usage: 14.2 MB
# Your runtime beats 90.15 % of python3 submissions.
# Your memory usage beats 87.22 % of python3 submissions.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        edges = {i:[] for i in range(numCourses)}
        
        for i, j in prerequisites:
            indegrees[i] += 1
            edges[j].append(i)
        
        queue = collections.deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
                
        ans = []
        
        while queue:
            course = queue.popleft()
            ans.append(course)
            for i in edges[course]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        
        if len(ans) != numCourses:
            return []
        return ans