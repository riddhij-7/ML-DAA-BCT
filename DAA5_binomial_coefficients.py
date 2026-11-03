n = int(input("Enter n: "))
k = int(input("Enter k: "))

C = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(min(i, k) + 1):
        if j == 0 or j == i:
            C[i][j] = 1                                 # base case
        else:
            C[i][j] = C[i-1][j-1] + C[i-1][j]           # Pascal's rule

print(f"C({n}, {k}) =", C[n][k])
print("Table:")
for row in C:
    print(row)

#Input-5, 2	Output-C(5, 2) = 10 