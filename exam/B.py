n = int(input())
heights = list(map(int, input().split()))

stack = []
max_area = 0

for i in range(0, n + 1):
    while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
        h = heights[stack.pop()]
        w =  i if len(stack) == 0 else i - 1 - stack[-1]
        max_area = max(max_area, h * w)

    stack.append(i)

print(max_area)