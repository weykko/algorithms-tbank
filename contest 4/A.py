n = int(input())
array = list(map(int, input().split()))

prefix_sum = [0]
prefix_xor = [0]
for a in array:
    prefix_sum.append(prefix_sum[-1] + a)
    prefix_xor.append(prefix_xor[-1] ^ a)

m = int(input())

for _ in range(m):
    q, l, r = map(int, input().split())
    if q == 1:
        segment_sum = prefix_sum[r] - prefix_sum[l - 1]
        print(segment_sum)
    else:
        segment_xor = prefix_xor[r] ^ prefix_xor[l - 1]
        print(segment_xor)