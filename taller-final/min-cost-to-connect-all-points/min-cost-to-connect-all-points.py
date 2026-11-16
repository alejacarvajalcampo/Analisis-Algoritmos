class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        heap = [(0, 0)]
        total_cost = 0
        
        while len(visited) < n:
            cost, u = heapq.heappop(heap)
            
            if u in visited:
                continue
                
            visited.add(u)
            total_cost += cost
            
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap, (dist, v))
                    
        return total_cost