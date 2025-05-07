def dijkstra(graph, start, limit):
    import heapq

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    heapq.heapify(pq)

    while pq:
        dist, u = heapq.heappop(pq)
        if dist > distances[u]: continue
        for v, w, l in graph[u]:
            next_dist = dist + w
            if l >= limit and next_dist < distances[v]:
                distances[v] = next_dist
                heapq.heappush(pq, (next_dist, v))

    return distances


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
max_cups = 0
for _ in range(m):
    u, v, w, l = map(int, input().split())
    cups = (l - 3_000_000) // 100
    max_cups = max(cups, max_cups)
    graph[u].append((v, w, cups))
    graph[v].append((u, w, cups))

left, right = 0, max_cups
result = 0
while left <= right:
    mid = (left + right) // 2
    cur_cost = dijkstra(graph, 1, mid)[n]
    if cur_cost <= 1440:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)
