import java.util.*;
import java.io.*;

public class E {
    static class MySegmentTree {
        int n;
        int[] st;
        int[] xorTag;
        int neutral = 0;

        public MySegmentTree(int[] a) {
            n = a.length;
            int size = 4 * n;
            st = new int[size];
            xorTag = new int[size];
            build(a, 1, 0, n - 1);
        }

        private void build(int[] a, int node, int l, int r) {
            if (l == r) {
                st[node] = a[l];
            } else {
                int mid = (l + r) / 2;
                build(a, 2 * node, l, mid);
                build(a, 2 * node + 1, mid + 1, r);
                st[node] = operation(st[2 * node], st[2 * node + 1]);
            }
        }

        private int operation(int x, int y) {
            return x + y;
        }

        private void push(int node, int l, int r) {
            if (xorTag[node] != 0) {
                st[node] = (r - l + 1) - st[node];
                if (l != r) {
                    xorTag[2 * node] ^= 1;
                    xorTag[2 * node + 1] ^= 1;
                }
                xorTag[node] = 0;
            }
        }

        public void rangeXor(int ql, int qr) {
            rangeXor(1, 0, n - 1, ql, qr);
        }

        private void rangeXor(int node, int l, int r, int ql, int qr) {
            push(node, l, r);
            if (qr < l || r < ql) {
                return;
            }
            if (ql <= l && r <= qr) {
                xorTag[node] = 1;
                push(node, l, r);
                return;
            }
            int m = (l + r) / 2;
            rangeXor(2 * node, l, m, ql, qr);
            rangeXor(2 * node + 1, m + 1, r, ql, qr);
            st[node] = operation(st[2 * node], st[2 * node + 1]);
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
            return operation(
                    query(2 * node, l, m, ql, qr),
                    query(2 * node + 1, m + 1, r, ql, qr)
            );
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        int q = Integer.parseInt(br.readLine());

        MySegmentTree[] segmentTrees = new MySegmentTree[20];
        for (int bit = 0; bit < 20; bit++) {
            int[] bitArray = new int[n];
            for (int j = 0; j < n; j++) {
                bitArray[j] = (a[j] >> bit) & 1;
            }
            segmentTrees[bit] = new MySegmentTree(bitArray);
        }

        List<Long> results = new ArrayList<>();

        for (int i = 0; i < q; i++) {
            String[] query = br.readLine().split(" ");
            int l = Integer.parseInt(query[1]) - 1;
            int r = Integer.parseInt(query[2]) - 1;

            if (query[0].equals("1")) {
                long sum = 0;
                for (int bit = 0; bit < 20; bit++) {
                    int bitCount = segmentTrees[bit].query(l, r);
                    sum += (long) bitCount * (1L << bit);
                }
                results.add(sum);
            } else {
                int x = Integer.parseInt(query[3]);
                for (int bit = 0; bit < 20; bit++) {
                    if (((x >> bit) & 1) == 1) {
                        segmentTrees[bit].rangeXor(l, r);
                    }
                }
            }
        }

        for (long res : results) {
            System.out.println(res);
        }
    }
}
