# код верен, но TL, поэтому используем быстрый Java ^_^
class MySegmentTree:
    def __init__(self, a):
        self.n = len(a)
        self.a = a
        size = 4 * self.n
        self.st = [0] * size
        self.plus_tag = [0] * size
        self.neutral = float('inf')

    def __operation(self, x, y):
        return min(x, y)

    def __push(self, node, l, r):
        if self.plus_tag[node] == 0: return

        v = self.plus_tag[node]
        self.st[node] += v
        if l != r:
            self.plus_tag[node * 2] += v
            self.plus_tag[node * 2 + 1] += v

        self.plus_tag[node] = 0

    def range_plus(self, ql, qr, v):
        self.__range_plus(1, 0, self.n - 1, ql, qr, v)

    def __range_plus(self, node, l, r, ql, qr, v):
        self.__push(node, l, r)
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.plus_tag[node] += v
            self.__push(node, l, r)
        else:
            m = (l + r) // 2
            self.__range_plus(node * 2, l, m, ql, qr, v)
            self.__range_plus(node * 2 + 1, m + 1, r, ql, qr, v)
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
        if q[3] == '0':
            continue
        st.range_plus(int(q[1]), int(q[2]) - 1, int(q[3]))
    else:
        print(st.query(int(q[1]), int(q[2]) - 1))