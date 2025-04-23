class MySegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.array = array
        self.neutral = 0
        self.segment_tree = [self.neutral for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            self.segment_tree[node] = self.array[l]
        else:
            mid = (l + r) // 2
            self.build(2 * node, l, mid)
            self.build(2 * node + 1, mid + 1, r)
            self.segment_tree[node] = self.operation(self.segment_tree[2 * node], self.segment_tree[2 * node + 1])

    def operation(self, x, y):
        return x + y

    def query(self, l, r):
        return self.query_internal(1, 0, self.n - 1, l, r)

    def update(self, idx, val):
        return self.update_internal(1, 0, self.n - 1, idx, val)

    def update_internal(self, node, l, r, idx, val):
        if l == r:
            self.array[idx] = val
            self.segment_tree[node] = val
        else:
            mid = (l + r) // 2
            if l <= idx <= mid:
                self.update_internal(2 * node, l, mid, idx, val)
            else:
                self.update_internal(2 * node + 1, mid + 1, r, idx, val)
            self.segment_tree[node] = self.operation(self.segment_tree[2 * node], self.segment_tree[2 * node + 1])

    def query_internal(self, node, tl, tr, l, r):
        if r < tl or tr < l:
            return self.neutral
        if l <= tl and tr <= r:
            return self.segment_tree[node]
        tm = (tl + tr) // 2
        return self.operation(self.query_internal(2 * node, tl, tm, l, r),
                              self.query_internal(2 * node + 1, tm + 1, tr, l, r))


n, m = map(int, input().split())
array = list(map(int, input().split()))
segment_tree = MySegmentTree(array)

for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        segment_tree.update(q[1], q[2])
    else:
        print(segment_tree.query(q[1], q[2] - 1))
