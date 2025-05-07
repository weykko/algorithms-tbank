class MyDisjointSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)

        if x_set == y_set:
            return False
        if self.rank[x_set] < self.rank[y_set]:
            x_set, y_set = y_set, x_set
        self.parent[y_set] = x_set
        if self.rank[x_set] == self.rank[y_set]:
            self.rank[x_set] += 1

        return True


n, m = map(int, input().split())
dset = MyDisjointSet(n + 1)
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

result = 0
for u, v, w in sorted(edges, key=lambda x: x[2]):
    if dset.union(u, v):
        result += w
        n -= 1
        if n == 1:
            break

print(result)
