lo, hi, steps = 0, n - 1, 0
while lo <= hi:
    mid = (lo + hi) // 2
    steps += 1
    if scores[mid] == target:
        print("Binary search  : index =", mid, "| steps =", steps, "| O(log n)")
        break
    elif scores[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
print()