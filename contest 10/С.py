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
dset = MyDisjointSet(((n + 1) * (m + 1)) + 1)
for i in range(1, n + 1):
    states = input().split()
    for j in range(1, m + 1):
        state = states[j - 1]
        if state == '0': continue
        p = m * (i - 1) + j
        if state != '1':
            dset.union(p, p + 1)
        if state != '2':
            dset.union(p, p + m)

added = []
cost = 0

for i in range(1, n):
    for j in range(1, m + 1):
        p = m * (i - 1) + j
        if dset.union(p, p + m):
            added.append((i, j, 1))
            cost += 1

for i in range(1, n + 1):
    for j in range(1, m):
        p = m * (i - 1) + j
        if dset.union(p, p + 1):
            added.append((i, j, 2))
            cost += 2

print(len(added), cost)
for a in added:
    print(' '.join(map(str, a)))