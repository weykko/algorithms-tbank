class MySegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.array = array
        self.neutral = [0, -1]
        self.segment_tree = [self.neutral for _ in range(4 * self.n)]
        self.__build(1, 0, self.n - 1)

    def __build(self, node, l, r):
        if l == r:
            self.segment_tree[node] = [self.array[l], l]
        else:
            mid = (l + r) // 2
            self.__build(2 * node, l, mid)
            self.__build(2 * node + 1, mid + 1, r)
            self.segment_tree[node] = self.__operation(self.segment_tree[2 * node], self.segment_tree[2 * node + 1])

    def __operation(self, x, y): return [x[0] + y[0], 666]

    def query(self, k):
        current_node = 1
        while True:
            if self.segment_tree[current_node][0] < k:
                return -1
            elif current_node * 2 >= len(self.segment_tree) or self.segment_tree[current_node * 2] == self.neutral:
                return self.segment_tree[current_node][1]
            elif current_node * 2 + 1 == len(self.segment_tree) or self.segment_tree[current_node * 2 + 1] == self.neutral:
                current_node *= 2
            else:
                left = 2 * current_node
                right = 2 * current_node + 1
                if self.segment_tree[left][0] >= k:
                    current_node = left
                else:
                    current_node = right
                    k -= self.segment_tree[left][0]

    def update(self, idx):
        val = int(self.array[idx] == 0)
        return self.__update_internal(1, 0, self.n - 1, idx, val)

    def __update_internal(self, node, l, r, idx, val):
        if l == r:
            self.array[idx] = val
            self.segment_tree[node] = [val, l]
        else:
            mid = (l + r) // 2
            if l <= idx <= mid:
                self.__update_internal(2 * node, l, mid, idx, val)
            else:
                self.__update_internal(2 * node + 1, mid + 1, r, idx, val)
            self.segment_tree[node] = self.__operation(self.segment_tree[2 * node], self.segment_tree[2 * node + 1])


n, m = map(int, input().split())
array = list(map(int, input().split()))
segment_tree = MySegmentTree(array)

for _ in range(m):
    q = input().split()
    if q[0] == '1':
        segment_tree.update(int(q[1]))
    else:
        print(segment_tree.query(int(q[1]) + 1))
