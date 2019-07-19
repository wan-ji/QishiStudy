# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/


# Solution 1
# Runtime: 100 ms
# Memory Usage: 19.8 MB
# Your runtime beats 31.10 % of python3 submissions.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = {i:[] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v,w))
        
        heap = []
        for v, w in graph[src]:
            heapq.heappush(heap, (w, v, 0))
        
        while heap:
            w, v, nstop = heapq.heappop(heap)
            if v == dst:
                return w
            if nstop < K:
                for v2, w2 in graph[v]:
                    heapq.heappush(heap, (w2 + w, v2, nstop + 1))
            
        return -1
