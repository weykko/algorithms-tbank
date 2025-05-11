class LCA:
    def __init__(self, parents, depths, tree_depth):
        import math

        self.n = len(parents)
        self.d = depths
        self.max_deg = math.ceil(math.log2(tree_depth))
        self.dp = [[0] * (self.max_deg + 1) for _ in range(self.n)]
        self.dp_min = [[float('inf')] * (self.max_deg + 1) for _ in range(self.n)]

        for j in range(0, self.max_deg + 1):
            for i in range(self.n):
                if j == 0:
                    self.dp[i][j] = parents[i][0]
                    self.dp_min[i][j] = parents[i][1]
                else:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]
                    self.dp_min[i][j] = min(self.dp_min[self.dp[i][j - 1]][j - 1], self.dp_min[i][j - 1])

    def query(self, u, v):
        if self.d[v] > self.d[u]: u, v = v, u
        u_min, v_min = float('inf'), float('inf')

        for i in range(self.max_deg, -1, -1):
            if self.d[self.dp[u][i]] >= self.d[v]:
                u_min = min(self.dp_min[u][i], u_min)
                u = self.dp[u][i]

        if v == u: return min(u_min, v_min)

        for i in range(self.max_deg, -1, -1):
            if self.dp[v][i] != self.dp[u][i]:
                v_min = min(self.dp_min[v][i], v_min)
                u_min = min(self.dp_min[u][i], u_min)
                v = self.dp[v][i]
                u = self.dp[u][i]

        return min(u_min, v_min, self.dp_min[v][0], self.dp_min[u][0])


n = int(input())
parents = [(0, float('inf'))] * n
depths = [0] * n
tree_depth = 0

for i in range(1, n):
    p, w = map(int, input().split())
    parents[i] = p, w
    depths[i] = depths[p] + 1
    tree_depth = max(tree_depth, depths[i])

lca = LCA(parents, depths, tree_depth)
m = int(input())

for _ in range(m):
    u, v = map(int, input().split())
    print(lca.query(u, v))