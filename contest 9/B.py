class MySegmentTree:
    def __init__(self, a):
        self.n = len(a)
        self.a = a
        size = 4 * self.n
        self.st = [0] * size
        self.add_tag = [0] * size
        self.set_tag = [-1] * size
        self.neutral = 0
    #     self.__build(1, 0, self.n - 1)

    def __build(self, node, l, r):
        if l == r:
            self.st[node] = self.a[l]
        else:
            mid = (l + r) // 2
            self.__build(2 * node, l, mid)
            self.__build(2 * node + 1, mid + 1, r)
            self.st[node] = self.__operation(self.st[2 * node], self.st[2 * node + 1])

    def __operation(self, x, y):
        return x + y

    def __push(self, node, l, r):
        if self.set_tag[node] != -1:
            v = self.set_tag[node]
            self.st[node] = v * (r - l + 1)
            if l != r:
                self.set_tag[node * 2] = v
                self.set_tag[node * 2 + 1] = v
                self.add_tag[node * 2] = 0
                self.add_tag[node * 2 + 1] = 0

            self.set_tag[node] = -1

        if self.add_tag[node] != 0:
            v = self.add_tag[node]
            self.st[node] += v * (r - l + 1)
            if l != r:
                self.add_tag[node * 2] += v
                self.add_tag[node * 2 + 1] += v

            self.add_tag[node] = 0

    def range_set(self, ql, qr, v):
        self.__range_set(1, 0, self.n - 1, ql, qr, v)

    def __range_set(self, node, l, r, ql, qr, v):
        self.__push(node, l, r)
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.set_tag[node] = v
            self.add_tag[node] = 0
            self.__push(node, l, r)
        else:
            m = (l + r) // 2
            self.__range_set(node * 2, l, m, ql, qr, v)
            self.__range_set(node * 2 + 1, m + 1, r, ql, qr, v)
            self.st[node] = self.__operation(self.st[node * 2], self.st[node * 2 + 1])

    def range_add(self, ql, qr, v):
        self.__range_add(1, 0, self.n - 1, ql, qr, v)

    def __range_add(self, node, l, r, ql, qr, v):
        self.__push(node, l, r)
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.add_tag[node] += v
            self.__push(node, l, r)
        else:
            m = (l + r) // 2
            self.__range_add(node * 2, l, m, ql, qr, v)
            self.__range_add(node * 2 + 1, m + 1, r, ql, qr, v)
            self.st[node] = self.__operation(self.st[node * 2], self.st[node * 2 + 1])

    def query(self, ql, qr):
        return self.__query(1, 0, self.n - 1, ql, qr)

    def __query(self, node, l, r, ql, qr):
        self.__push(node, l, r)
        if qr < l or r < ql:
            return self.neutral
        if ql <= l and r <= qr:
            return self.st[node]
        m = (l + r) // 2
        return self.__operation(self.__query(node * 2, l, m, ql, qr), self.__query(node * 2 + 1, m + 1, r, ql, qr))


n, m = map(int, input().split())
a = [0] * n
st = MySegmentTree(a)

for _ in range(m):
    q = input().split()
    if q[0] == '1':
        st.range_set(int(q[1]), int(q[2]) - 1, int(q[3]))
    elif q[0] == '2':
        if q[3] == '0':
            continue
        st.range_add(int(q[1]), int(q[2]) - 1, int(q[3]))
    else:
        print(st.query(int(q[1]), int(q[2]) - 1))
