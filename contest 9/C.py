class MySegmentTree:
    def __init__(self, a):
        self.n = len(a)
        self.a = a
        size = 2 * self.n
        self.neutral = (0, 0, False, False)
        self.st = [self.neutral] * size
        self.set_tag = [-1] * size

    def __operation(self, x, y):
        if x[3] and y[2]:
            return x[0] + y[0], x[1] + y[1] - 1, x[2], y[3]
        return x[0] + y[0], x[1] + y[1], x[2], y[3]

    def __push(self, node, l, r):
        if self.set_tag[node] != -1:
            v = self.set_tag[node]
            if v == 1:
                self.st[node] = (r - l + 1, 1, True, True)
            else:
                self.st[node] = (0, 0, False, False)
            if l != r:
                self.set_tag[node * 2] = v
                self.set_tag[node * 2 + 1] = v

            self.set_tag[node] = -1

    def range_set(self, ql, qr, v):
        self.__range_set(1, 0, self.n - 1, ql, qr, v)

    def __range_set(self, node, l, r, ql, qr, v):
        self.__push(node, l, r)
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.set_tag[node] = v
            self.__push(node, l, r)
        else:
            m = (l + r) // 2
            self.__range_set(node * 2, l, m, ql, qr, v)
            self.__range_set(node * 2 + 1, m + 1, r, ql, qr, v)
            self.st[node] = self.__operation(self.st[node * 2], self.st[node * 2 + 1])

    def query(self, ql, qr):
        return self.__query(1, 0, self.n - 1, ql, qr)[:2][::-1]

    def __query(self, node, l, r, ql, qr):
        self.__push(node, l, r)
        if qr < l or r < ql:
            return self.neutral
        if ql <= l and r <= qr:
            return self.st[node]
        m = (l + r) // 2
        return self.__operation(self.__query(node * 2, l, m, ql, qr), self.__query(node * 2 + 1, m + 1, r, ql, qr))


n = int(input())
a = [0] * (1 << 20)
ADDER = 500_000
st = MySegmentTree(a)

for _ in range(n):
    q = input().split()
    if q[0] == 'W':
        l = int(q[1]) + ADDER
        r = int(q[2]) + l - 1
        st.range_set(l, r, 0)
        print(' '.join(map(str, st.query(0, len(a)))))
    else:
        l = int(q[1]) + ADDER
        r = int(q[2]) + l - 1
        st.range_set(l, r, 1)
        print(' '.join(map(str, st.query(0, len(a)))))