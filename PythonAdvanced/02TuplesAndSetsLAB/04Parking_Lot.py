cars = int(input())
car_map = set()
for _ in range(cars):
    direction, number = input().split(sep=', ')
    if direction == "OUT":
        car_map.remove(number)
    else:
        car_map.add(number)

if car_map:
    for car in car_map:
        print(car)
else:
    print("Parking Lot is Empty")
