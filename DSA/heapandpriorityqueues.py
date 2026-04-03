# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)

import heapq
from collections import Counter

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

heapq.heapify(A)
print("After heapify:", A)

# Heap Push (Insert element)
# Time: O(log n)

heapq.heappush(A, 4)
print("After push:", A)

# Heap Pop (Extract min)
# Time: O(log n)

minn = heapq.heappop(A)
print("After pop:", A, "Min:", minn)


# Heap Sort
# Time: O(n log n), Space: O(n)

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        new_list[i] = heapq.heappop(arr)

    return new_list

print("Heap sort:", heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))


# Heap Push Pop
# Time: O(log n)

heapq.heappushpop(A, 99)
print("After pushpop:", A)


# Peek at Min
# Time: O(1)

print("Min element:", A[0])


# Max Heap (using negatives)

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
B = [-x for x in B]

heapq.heapify(B)
print("Max heap (stored as negatives):", B)

largest = -heapq.heappop(B)
print("Largest element:", largest)

heapq.heappush(B, -7)
print("After inserting 7:", B)


# Build heap from scratch
# Time: O(n log n)

C = [-5, 4, 2, 1, 7, 0, 3]
heap = []

for x in C:
    heapq.heappush(heap, x)
    print("Heap:", heap, "Size:", len(heap))


# Using tuples in heap

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]
counter = Counter(D)
print("Counter:", counter)

heap = []

for k, v in counter.items():
    heapq.heappush(heap, (v, k))

print("Heap with (freq, value):", heap)