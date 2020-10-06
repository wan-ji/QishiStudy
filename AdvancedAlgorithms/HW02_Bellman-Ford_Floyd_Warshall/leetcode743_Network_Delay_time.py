'''
Leetcode 787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

'''

class Solution:
    
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        '''
        Bellman-Ford Algorithm
        '''
        dist = [sys.maxsize] * (N+1)
        dist[K] = 0
        
        for _ in range(N-1):
            for u, v, w in times:
                dist[v] = min(dist[v], dist[u] + w)
        
        return max(dist[1:]) if max(dist[1:]) < sys.maxsize else -1

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        '''
        Dijkstra Algorithm
        '''
        dist = [sys.maxsize] * (N+1)
        dist[K] = 0
        
        visited = [False] * (N+1)
        
        graph = [defaultdict(int) for _ in range(N+1)]
        
        for u, v, w in times:
            graph[u][v] = w
        
        heap = [(0, K)]
        while heap:
            distance, node = heapq.heappop(heap)
            if not visited[node]:
                dist[node] = distance
                visited[node] = True
            
                for v, w in graph[node].items():
                    heapq.heappush(heap, (w + distance, v))


        return max(dist[1:]) if max(dist[1:]) < sys.maxsize else -1







