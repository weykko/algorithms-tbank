from collections import deque

n = int(input())
a = list(map(int, input().split()))
d = list(map(int, input().split()))

left = [0] * (n + 2)
right = [0] * (n + 2)
killed = [False] * (n + 2)
killed[0], killed[n + 1] = True, True
damage = [0] * (n + 2)
hp = [0] * (n + 2)
for i in range(n):
    damage[i + 1] = a[i]
    hp[i + 1] = d[i]

queue = deque()
for i in range(1, n + 1):
    left[i] = i - 1
    right[i] = i + 1
    if damage[left[i]] + damage[right[i]] > hp[i]:
        queue.append(i)
        killed[i] = True

result = []
while queue:
    for i in queue:
        right[left[i]] = right[i]
        left[right[i]] = left[i]

    level_size = len(queue)
    for _ in range(level_size):
        i = queue.popleft()
        for next in [left[i], right[i]]:
            if not killed[next] and damage[left[next]] + damage[right[next]] > hp[next]:
                queue.append(next)
                killed[next] = True

    result.append(level_size)

result.extend([0] * (n - len(result)))
print(' '.join(map(str, result)))