import java.util.*;

public class C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[1 << 20];
        final int ADDER = 500_000;
        MySegmentTree st = new MySegmentTree(a);

        while (n-- > 0) {
            String q = sc.next();
            int l = sc.nextInt() + ADDER;
            int r = sc.nextInt() + l - 1;
            if (q.equals("W")) {
                st.rangeSet(l, r, 0);
                int[] result = st.query(0, a.length);
                System.out.println(result[0] + " " + result[1]);
            } else {
                st.rangeSet(l, r, 1);
                int[] result = st.query(0, a.length);
                System.out.println(result[0] + " " + result[1]);
            }
        }
    }
}

class MySegmentTree {
    private int n;
    private final int[][] st;
    private final int[] setTag;
    private final int[] neutral = {0, 0, 0, 0};

    public MySegmentTree(int[] a) {
        this.n = a.length;
        int size = 2 * this.n;
        this.st = new int[size][];
        Arrays.fill(st, neutral);
        this.setTag = new int[size];
        Arrays.fill(setTag, -1);
    }

    private int[] operation(int[] x, int[] y) {
        var segments = x[3] + y[2] == 2 ? x[0] + y[0] - 1 : x[0] + y[0];
        return new int[]{segments, x[1] + y[1], x[2], y[3]};
    }

    private void push(int node, int l, int r) {
        if (setTag[node] != -1) {
            int v = setTag[node];
            if (v == 1) {
                st[node] = new int[]{1, r - l + 1, 1, 1};
            } else {
                st[node] = new int[]{0, 0, 0, 0};
            }
            if (l != r) {
                setTag[node * 2] = v;
                setTag[node * 2 + 1] = v;
            }
            setTag[node] = -1;
        }
    }

    public void rangeSet(int ql, int qr, int v) {
        rangeSet(1, 0, n - 1, ql, qr, v);
    }

    private void rangeSet(int node, int l, int r, int ql, int qr, int v) {
        push(node, l, r);
        if (qr < l || r < ql) {
            return;
        }
        if (ql <= l && r <= qr) {
            setTag[node] = v;
            push(node, l, r);
        } else {
            int m = (l + r) / 2;
            rangeSet(node * 2, l, m, ql, qr, v);
            rangeSet(node * 2 + 1, m + 1, r, ql, qr, v);
            st[node] = operation(st[node * 2], st[node * 2 + 1]);
        }
    }

    public int[] query(int ql, int qr) {
        return query(1, 0, n - 1, ql, qr);
    }

    private int[] query(int node, int l, int r, int ql, int qr) {
        push(node, l, r);
        if (qr < l || r < ql) {
            return neutral;
        }
        if (ql <= l && r <= qr) {
            return st[node];
        }
        int m = (l + r) / 2;
        return operation(query(node * 2, l, m, ql, qr), query(node * 2 + 1, m + 1, r, ql, qr));
    }
}
