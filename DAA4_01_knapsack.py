n = int(input("Number of items: "))
val, wt = [], []
for i in range(n):
    val.append(int(input(f"Value of item {i+1}: ")))
    wt.append(int(input(f"Weight of item {i+1}: ")))
W = int(input("Capacity of knapsack: "))

# build the table
dp = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(W + 1):
        dp[i][w] = dp[i-1][w]                                          # skip item i
        if wt[i-1] <= w:                                               # or take item i
            dp[i][w] = max(dp[i][w], val[i-1] + dp[i-1][w - wt[i-1]])

# find which items were taken (walk back through the table)
chosen, w = [], W
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        chosen.append(i)
        w -= wt[i-1]

print("Maximum value:", dp[n][W])
print("Items taken:", chosen[::-1])

#Input 3, then for each item (value, weight):
#60 10
#100 20
#120 30
#then capacity 50
#Output - max value 220, items taken [2, 3]