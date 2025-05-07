def dijkstra(graph, start):
    import heapq

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    heapq.heapify(pq)

    while pq:
        dist, u = heapq.heappop(pq)
        if dist > distances[u]: continue
        for v, w in graph[u]:
            next_dist = dist + w
            if next_dist < distances[v]:
                distances[v] = next_dist
                heapq.heappush(pq, (next_dist, v))

    return distances


n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v, w = map(int, input().split())
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))

distances = dijkstra(graph, 1)
for i in range(1, n + 1):
    print(distances[i], end=' ')
