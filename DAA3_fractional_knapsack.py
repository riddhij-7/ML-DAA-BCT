n = int(input("Number of items: "))
items = []
for i in range(n):
    w = int(input(f"Weight of item {i+1}: "))
    p = int(input(f"Profit of item {i+1}: "))
    items.append((p / w, w, p, i + 1))            # (ratio, weight, profit, item no.)
capacity = int(input("Capacity of knapsack: "))

items.sort(reverse=True)                           # best ratio first
total = 0

for ratio, w, p, no in items:
    if capacity == 0:
        break
    take = min(w, capacity)                        # full item, or the part that fits
    total += p * take / w
    capacity -= take
    print(f"Item {no}: took {take} of {w}")

print("Maximum profit:", total)

#Input - 3, then for each item (weight, profit):
#10 60
#20 100
#30 120
#then capacity 50
#Item 1: 10 of 10, Item 2: 20 of 20, Item 3: 20 of 30, max profit 240.0