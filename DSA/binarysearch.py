A = [-3, -1, 0, 1, 4, 7]

# Naive O(n) searching
if 8 in A:
  print(True)


# Traditional Binary Search - Looking up if number is in array:
# Time: O(log n)
# Space: O(1)

def binary_search(arr, target):
  N = len(arr)
  L = 0
  R = N - 1

  while L <= R:
    M = L + ((R-L) // 2)

    if arr[M] == target:
      return True
    elif target < arr[M]:
      R = M - 1
    else:
      L = M + 1

  return False

binary_search(A, 8)


# Condition based
B = [False, False, False, False, True]

def binary_search_condition(arr):
  N = len(arr)
  L = 0
  R = N - 1

  while L < R:
    M = (L + R) // 2

    if arr[M]:
      R = M
    else:
      L = M + 1

  return L

binary_search_condition(B)


# Range-Based

def guess_number(target, L, R):
    while L <= R:
        M = (L + R) // 2
        if M == target:
            return M  # Found the number
        elif M < target:
            L = M + 1
        else:
            R = M - 1
    return -1  # Target not found


target = 2
result = guess_number(target, 1, 100)
print(f"The guessed number is: {result}")