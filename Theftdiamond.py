n = int(input())
cameras = []
for _ in range(n):
    t, s = map(int, input().split())
    cameras.append((t, s))

# Sort cameras by their disable time in ascending order
cameras.sort(key=lambda x: x[1])

# Initialize variables to keep track of state
diamonds_stolen = [False, False]
time = 0
disabled_cameras = {1: [], 2: []}

# Iterate through the cameras
for t, s in cameras:
    if not diamonds_stolen[0]:
        if t == 1:
            diamonds_stolen[0] = True
        elif t == 3 and len(disabled_cameras[1]) > 0:
            diamonds_stolen[0] = True

    if not diamonds_stolen[1]:
        if t == 2:
            diamonds_stolen[1] = True
        elif t == 3 and len(disabled_cameras[2]) > 0:
            diamonds_stolen[1] = True

    if diamonds_stolen[0] and diamonds_stolen[1]:
        break

    if t != 3:
        disabled_cameras[t].append(s)

    time += 1

# If both diamonds are stolen, print the time taken, otherwise print -1
if diamonds_stolen[0] and diamonds_stolen[1]:
    print(time)
else:
    print(-1)
