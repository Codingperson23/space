scores = [12, 25, 33, 41, 50, 67, 72, 85, 91, 98]
n, target = len(scores), 98
print("=== Quiz Score Finder (n =", n, ", scores) ===")
print("Scores:", scores, "| Target:", target)
print()


steps = 0
for i in range(n):
    steps += 1
    if scores[i] == target:
        print("Linear search  : index =", i, "| steps =", steps, "| O(n)")
        break
print()