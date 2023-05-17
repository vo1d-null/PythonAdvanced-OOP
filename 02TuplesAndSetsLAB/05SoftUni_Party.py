n = int(input())
reservations = set()
for _ in range(n):
    reservations_num = input()
    reservations.add(reservations_num)

guest_reservation_num = input()
while guest_reservation_num != "END":
    reservations.remove(guest_reservation_num)
    guest_reservation_num = input()

print(len(reservations))
for num in sorted(reservations):
    print(num)