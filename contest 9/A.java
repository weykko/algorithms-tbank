import java.util.*;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] a = new int[n];
        MySegmentTree st = new MySegmentTree(a);

        sc.nextLine();
        for (int i = 0; i < m; i++) {
            String[] q = sc.nextLine().split(" ");
            if (q[0].equals("1")) {
                if (q[3].equals("0")) {
                    continue;
                }
                st.rangeSet(Integer.parseInt(q[1]), Integer.parseInt(q[2]) - 1, Integer.parseInt(q[3]));
            } else {
                System.out.println(st.query(Integer.parseInt(q[1]), Integer.parseInt(q[2]) - 1));
            }
        }

        sc.close();
    }
}

class MySegmentTree {
    private int n;
    private int[] st;
    private int[] plusTag;
    private final int neutral = Integer.MAX_VALUE;

    public MySegmentTree(int[] a) {
        this.n = a.length;
        int size = 4 * this.n;
        this.st = new int[size];
        this.plusTag = new int[size];
    }

    private int operation(int x, int y) {
        return Math.min(x, y);
    }

    private void push(int node, int l, int r) {
        if (plusTag[node] == 0) return;

        int v = plusTag[node];
        st[node] += v;
        if (l != r) {
            plusTag[node * 2] += v;
            plusTag[node * 2 + 1] += v;
        }
        plusTag[node] = 0;
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
            plusTag[node] += v;
            push(node, l, r);
        } else {
            int m = (l + r) / 2;
            rangeSet(node * 2, l, m, ql, qr, v);
            rangeSet(node * 2 + 1, m + 1, r, ql, qr, v);
            st[node] = operation(st[node * 2], st[node * 2 + 1]);
        }
    }

    public int query(int ql, int qr) {
        return query(1, 0, n - 1, ql, qr);
    }

    private int query(int node, int l, int r, int ql, int qr) {
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
