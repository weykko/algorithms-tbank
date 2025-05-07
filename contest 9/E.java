import java.util.*;

public class E {
    static class Point {
        long x, y, z;
        int op;
        Point(long xx, long yy) { x = xx; y = yy; }
        Point(long xx, long yy, long zz, int oo) { x = xx; y = yy; z = zz; op = oo; }
    }

    static class Line {
        Point s, e;
        Line(Point ss, Point ee) { s = ss; e = ee; }
    }

    static class BIT {
        long[] sum;
        int size;
        BIT(int n) {
            size = n;
            sum = new long[n+2];
        }
        long lowbit(long x) {
            return x & (-x);
        }
        void add(int x, long c) {
            while (x <= size) {
                sum[x] += c;
                x += lowbit(x);
            }
        }
        long getsum(int x) {
            long ans = 0;
            while (x > 0) {
                ans += sum[x];
                x -= (int)lowbit(x);
            }
            return ans;
        }
    }

    static final int MAXN = 500000 + 5;
    static Point[] pt = new Point[MAXN * 4];
    static Line[] shu = new Line[MAXN], heng = new Line[MAXN];
    static long[] id = new long[MAXN * 4];
    static Map<Long, Integer> maps = new HashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long ans = 0;
        int idx = 0;
        int cnt = 0;
        int na = 0, nb = 0, naa = 0, nbb = 0;

        for (int i = 0; i < n; i++) {
            long x1 = sc.nextLong();
            long y1 = sc.nextLong();
            long x2 = sc.nextLong();
            long y2 = sc.nextLong();
            if (x1 == x2) {
                if (y1 > y2) { long temp = y1; y1 = y2; y2 = temp; }
                shu[na++] = new Line(new Point(x1, y1), new Point(x2, y2));
            } else {
                if (x1 > x2) { long temp = x1; x1 = x2; x2 = temp; }
                heng[nb++] = new Line(new Point(x1, y1), new Point(x2, y2));
            }
        }

        Arrays.sort(shu, 0, na, new Comparator<Line>() {
            public int compare(Line a, Line b) {
                if (a.s.x == b.s.x) return Long.compare(a.s.y, b.s.y);
                return Long.compare(a.s.x, b.s.x);
            }
        });

        Arrays.sort(heng, 0, nb, new Comparator<Line>() {
            public int compare(Line a, Line b) {
                if (a.s.y == b.s.y) return Long.compare(a.s.x, b.s.x);
                return Long.compare(a.s.y, b.s.y);
            }
        });

        for (int i = 1; i < na; i++) {
            if (shu[i].s.x != shu[i-1].s.x ||
                    (shu[i].s.x == shu[i-1].s.x && shu[i-1].e.y < shu[i].s.y)) {
                shu[naa++] = shu[i-1];
            } else {
                shu[i].s.y = Math.min(shu[i].s.y, shu[i-1].s.y);
                shu[i].e.y = Math.max(shu[i].e.y, shu[i-1].e.y);
            }
        }
        if (na > 0) shu[naa++] = shu[na-1];

        for (int i = 1; i < nb; i++) {
            if (heng[i].s.y != heng[i-1].s.y ||
                    (heng[i].s.y == heng[i-1].s.y && heng[i-1].e.x < heng[i].s.x)) {
                heng[nbb++] = heng[i-1];
            } else {
                heng[i].s.x = Math.min(heng[i].s.x, heng[i-1].s.x);
                heng[i].e.x = Math.max(heng[i].e.x, heng[i-1].e.x);
            }
        }
        if (nb > 0) heng[nbb++] = heng[nb-1];

        for (int i = 0; i < naa; i++) {
            long x1 = shu[i].s.x, y1 = shu[i].s.y, x2 = shu[i].e.x, y2 = shu[i].e.y;
            pt[cnt++] = new Point(x1, y1, y2, 1);
            id[idx++] = y1;
            id[idx++] = y2;
            ans += y2 - y1 + 1;
        }

        for (int i = 0; i < nbb; i++) {
            long x1 = heng[i].s.x, y1 = heng[i].s.y, x2 = heng[i].e.x, y2 = heng[i].e.y;
            pt[cnt++] = new Point(x1, y1, 1, 0);
            pt[cnt++] = new Point(x2 + 1, y2, -1, 0);
            id[idx++] = y1;
            ans += x2 - x1 + 1;
        }

        long tot = 0;
        Arrays.sort(id, 0, idx);
        int uniqueIdx = 0;
        for (int i = 0; i < idx; i++) {
            if (i == 0 || id[i] != id[i-1]) {
                id[uniqueIdx++] = id[i];
            }
        }
        idx = uniqueIdx;

        for (int i = 0; i < idx; i++) {
            maps.put(id[i], i + 1);
        }

        Arrays.sort(pt, 0, cnt, new Comparator<Point>() {
            public int compare(Point a, Point b) {
                if (a.x == b.x) return Integer.compare(a.op, b.op);
                return Long.compare(a.x, b.x);
            }
        });

        BIT bit = new BIT(MAXN * 4);
        for (int i = 0; i < cnt; i++) {
            if (pt[i].op == 0) {
                bit.add(maps.get(pt[i].y), pt[i].z);
            } else {
                tot += bit.getsum(maps.get(pt[i].z)) - bit.getsum(maps.get(pt[i].y) - 1);
            }
        }

        System.out.println(ans - tot);
    }
}