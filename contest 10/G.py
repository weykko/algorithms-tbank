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
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

a, b, c = map(int, input().split())
cost_a = dijkstra(graph, a)
cost_b = dijkstra(graph, b)
cost_c = dijkstra(graph, c)

total_cost = min(cost_a[b] + cost_b[c], cost_a[c] + cost_c[b], cost_b[a] + cost_a[c])
print(total_cost if total_cost != float('inf') else -1)
