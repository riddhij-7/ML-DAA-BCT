n = int(input("Number of jobs: "))
jobs = []
for i in range(n):
    job_id = input(f"Job {i+1} id: ")
    deadline = int(input("  deadline: "))
    profit = int(input("  profit: "))
    jobs.append((job_id, deadline, profit))

jobs.sort(key=lambda j: j[2], reverse=True)       # highest profit first
slots = [None] * max(j[1] for j in jobs)          # one slot per time unit
total = 0

for job_id, deadline, profit in jobs:
    for t in range(deadline - 1, -1, -1):         # latest free slot <= deadline
        if slots[t] is None:
            slots[t] = job_id
            total += profit
            break                                  # job placed, go to next job

print("Schedule (slot 1, 2, ...):", slots)
print("Maximum profit:", total)

#Input 5, then for each job (id, deadline, profit): a 2 100, b 1 19, c 2 27, d 1 25, e 3 15
#Output Schedule ['c', 'a', 'e'], max profit 142