# class Heap:
#     def __init__(self):
#         self.heap = []



n = int(input())
heap = []

for _ in range(n):
    t = input().split()
    if t[0] == '0':
        heap.append(int(t[1]))
        i = len(heap) - 1
        while i > 0 and heap[(i - 1) // 2] < heap[i]:
            heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
            i = (i - 1) // 2
    else:
        print(heap[0])
        heap[0] = heap[-1]
        heap.pop()
        i = 0
        while (2 * i + 1 < len(heap) and heap[2 * i + 1] > heap[i]) or (2 * i + 2 < len(heap) and heap[2 * i + 2] > heap[i]):
            if 2 * i + 2 < len(heap) and heap[2 * i + 2] >= heap[2 * i + 1]:
                heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]
                i = 2 * i + 2
            else:
                heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                i = 2 * i + 1