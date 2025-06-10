def can_test(comps, time, n):
    total_n = 0
    tasks = []
    for comp in comps:
        comp_n = get_n_count(*comp, time)
        total_n += comp_n
        tasks.append(comp_n)

    return total_n >= n, tasks


def get_n_count(t, b, y, time):
    unit = (t * b + y)
    return (time // unit) * b + min(time % unit, t * b) // t


n, m = map(int, input().split())
comps = [[int(x) for x in input().split()] for _ in range(m)]

left, right = 1, 2**64
time = float('inf')
result = []

while left <= right:
    mid = (left + right) // 2
    can, tasks = can_test(comps, mid, n)
    if can:
        right = mid - 1
        time = min(time, mid)
        result = tasks
    else:
        left = mid + 1

print(time)
print(' '.join(map(str, result)))