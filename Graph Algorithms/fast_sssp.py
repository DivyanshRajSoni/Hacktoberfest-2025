import heapq
from collections import defaultdict

class FastSSSP:
    def __init__(self, graph):
        self.graph = graph
        self.dist = defaultdict(lambda: float('inf'))
        self.prev = {}

    def run(self, source):
        self.dist[source] = 0
        pq = [(0, source)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > self.dist[u]:
                continue
            for v, weight in self.graph[u]:
                alt = d + weight
                if alt < self.dist[v]:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heapq.heappush(pq, (alt, v))
        return self.dist, self.prev

    def get_path(self, target):
        path = []
        while target in self.prev:
            path.append(target)
            target = self.prev[target]
        path.append(target)
        return path[::-1]

# Example usage
if __name__ == "__main__":
    graph = defaultdict(list)
    graph['A'].extend([('B', 1), ('C', 4)])
    graph['B'].extend([('C', 2), ('D', 5)])
    graph['C'].append(('D', 1))
    graph['D'].append(('E', 3))
    graph['E'].append(('A', 7))

    sssp = FastSSSP(graph)
    dist, prev = sssp.run('A')
    print("Shortest distances:", dict(dist))
    print("Shortest path to E:", sssp.get_path('E'))
