from collections import deque


def simulate_crossroads():
    green_light_duration = int(input())
    free_window_duration = int(input())

    cars_passed = 0
    command = input()
    cars_queue = deque()

    while command != "END":
        if command == "green":
            remaining_time = green_light_duration

            while remaining_time > 0 and (cars_queue or remaining_time == green_light_duration):
                if cars_queue:
                    car = cars_queue.popleft()
                    car_length = len(car)
                    if remaining_time >= car_length:
                        cars_passed += 1
                        remaining_time -= car_length
                    else:
                        character_hit = car[remaining_time]
                        print("A crash happened!")
                        print(f"{car} was hit at {character_hit}.")
                        return
                else:
                    remaining_time -= 1

            command = input()
            continue

        cars_queue.append(command)
        command = input()

    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")


simulate_crossroads()
