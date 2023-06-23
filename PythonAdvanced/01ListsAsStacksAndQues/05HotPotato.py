from collections import deque
kids_names = deque(input().split())
rotation_number = int(input()) -1
while len(kids_names) > 1:
    kids_names.rotate(-rotation_number)
    removed_kid = kids_names.popleft()
    print(f"Removed {removed_kid}")
print(f"Last is {kids_names.popleft()}")
