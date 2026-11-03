n = int(input("Enter n: "))

# ---------- Non-recursive ----------
a, b, steps = 0, 1, 0
print("Non-recursive series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b      # move to the next pair
    steps += 1           # count 1 step per loop run
print("\nNon-recursive steps =", steps)

# ---------- Recursive ----------
calls = 0
def fib(n):
    global calls
    calls += 1           # count 1 step per function call
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("Recursive series:", [fib(i) for i in range(n)])
print("Recursive steps =", calls)


# Input-10	Output-Series 0 1 1 2 3 5 8 13 21 34, non-recursive steps 10, recursive steps 276