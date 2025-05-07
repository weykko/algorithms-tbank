class MyDisjointSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.min = [i for i in range(n)]
        self.max = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)

        if x_set == y_set:
            return
        if self.rank[x_set] < self.rank[y_set]:
            self.parent[x_set] = y_set
        elif self.rank[x_set] > self.rank[y_set]:
            self.parent[y_set] = x_set
        else:
            self.parent[y_set] = x_set
            self.rank[x_set] = self.rank[x_set] + 1

        new_set = self.find(x)
        self.min[new_set] = min(self.min[x_set], self.min[y_set])
        self.max[new_set] = max(self.max[x_set], self.max[y_set])
        self.size[new_set] = (self.size[x_set] + self.size[y_set])

    def get(self, x):
        x_set = self.find(x)
        return self.min[x_set], self.max[x_set], self.size[x_set]


n, m = map(int, input().split())
dset = MyDisjointSet(n + 1)

for _ in range(m):
    q = input().split()
    if q[0] == 'union':
        dset.union(int(q[1]), int(q[2]))
    else:
        print(' '.join(map(str, dset.get(int(q[1])))))