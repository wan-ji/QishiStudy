'''
Leetcode 787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        '''
        Dijkstra algorithm
        '''
        graph = [collections.defaultdict(list) for _ in range(n)]
        
        for u, v, w in flights:
            graph[u][v] = w
        
        heap = []
        for v, w in graph[src].items():
            heap.append((w, v, 0))
        
        heapq.heapify(heap)
        while heap:
            cost, node, k = heapq.heappop(heap)
            
            if node == dst and k <= K:
                return cost
            if k >= K:
                continue
            k += 1
            for v, w in graph[node].items():
                heapq.heappush(heap, (cost + w, v, k))
                
        return -1