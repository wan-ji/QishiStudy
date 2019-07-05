973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/description/


# Divide and Conquer Solution 
# Runtime: 924 ms
# Memory Usage: 17 MB
# Your memory usage beats 83.59 % of python3 submissions.
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.dist2 = [self.distsquare(x) for x in points]
        idxlist = self.merge(points, 0, len(points) - 1, K)
        
        return [points[i] for i in idxlist]
    
    def merge(self, points, start, end, K):
        if start == end:
            return [start]
        
        mid = (start + end) // 2
        
        points1 = self.merge(points, start, mid, K)
        points2 = self.merge(points, mid + 1, end, K)
        
        ans = []
        idx1, idx2 = 0, 0
        while idx1 < len(points1) and idx2 < len(points2) and len(ans) < K:
            if self.dist2[points1[idx1]] <= self.dist2[points2[idx2]]:
                ans += [points1[idx1]]
                idx1 += 1
            else:
                ans += [points2[idx2]]
                idx2 += 1
        
        if len(ans) < K:
            if idx1 < len(points1):
                ans += points1[idx1:min(len(points1), idx1 + K - len(ans))]
            if idx2 < len(points2):
                ans += points2[idx2:min(len(points2), idx2 + K - len(ans))]
        
        return ans
        
    def distsquare(self, point):
        return point[0]*point[0] + point[1]*point[1]






# Runtime: 316 ms
# Memory Usage: 17 MB
# Your runtime beats 99.26 % of python3 submissions.
# Your memory usage beats 76.62 % of python3 submissions.
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = self.distsquare)
        return points[:K]
    
    def distsquare(self, point):
        return point[0]*point[0] + point[1]*point[1]