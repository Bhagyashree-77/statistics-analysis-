n, m = map(int, input().split())
programmers = list(map(int, input().split()))
projects = list(map(int, input().split()))

# Sort programmers and projects by stress tolerance and difficulty level
programmers = sorted(enumerate(programmers, start=1), key=lambda x: -x[1])
projects = sorted(enumerate(projects, start=1), key=lambda x: x[1])

# Initialize the assignment list
assignment = [[] for _ in range(m)]

for i in range(m):
    project_index, difficulty = projects[i]
    while programmers and programmers[0][1] >= difficulty:
        programmer_index, stress_tolerance = programmers.pop(0)
        assignment[i].append(programmer_index)

# If there are unassigned programmers, there is no valid assignment
if programmers:
    print("NO")
else:
    print("YES")
    for i in range(m):
        print(len(assignment[i]), *assignment[i])
