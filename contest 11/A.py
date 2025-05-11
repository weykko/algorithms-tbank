class LCA:
    def __init__(self, parents, depths):
        import math

        self.n = len(parents)
        self.d = depths
        self.max_deg = math.ceil(math.log2(self.n))
        self.dp = [[0] * (self.max_deg + 1) for _ in range(self.n)]

        for j in range(0, self.max_deg):
            for i in range(self.n):
                if j == 0: self.dp[i][j] = parents[i]
                else: self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def query(self, u, v):
        if self.d[v] > self.d[u]:
            u, v = v, u

        for i in range(self.max_deg, -1, -1):
            if self.d[self.dp[u][i]] >= self.d[v]:
                u = self.dp[u][i]

        if v == u: return v

        for i in range(self.max_deg, -1, -1):
            if self.dp[v][i] != self.dp[u][i]:
                v = self.dp[v][i]
                u = self.dp[u][i]

        return self.dp[v][0]


n = int(input())
parents = [0] * n
depths = [0] * n
ps = list(map(int, input().split()))

for i in range(1, n):
    p = ps[i - 1]
    parents[i] = p
    depths[i] = depths[p] + 1

lca = LCA(parents, depths)
m = int(input())

for _ in range(m):
    u, v = map(int, input().split())
    print(lca.query(u, v))