from heapq import heappop, heappush


def find_shortest_path(graph, start, end, closed_roads):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        (cost, node, path) = heappop(heap)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == end:
            return path, cost

        for neighbor, distance in graph[node]:
            if (node, neighbor) in closed_roads or (neighbor, node) in closed_roads:
                continue
            if neighbor not in visited:
                heappush(heap, (cost + distance, neighbor, path))

    return None, None


r = int(input())
roads = []
for _ in range(r):
    road_info = input().split(" - ")
    city1, city2, distance = road_info[0], road_info[1], int(road_info[2])
    roads.append((city1, city2, distance))

closed_roads_input = input()
closed_roads_list = closed_roads_input.split(",")
closed_roads = set()
for road in closed_roads_list:
    city1, city2 = road.split("-")
    closed_roads.add((city1, city2))
    closed_roads.add((city2, city1))

start_city = input()
end_city = input()

graph = {}
for road in roads:
    city1, city2, distance = road
    if city1 not in graph:
        graph[city1] = []
    if city2 not in graph:
        graph[city2] = []
    graph[city1].append((city2, distance))
    graph[city2].append((city1, distance))

shortest_path, total_distance = find_shortest_path(graph, start_city, end_city, closed_roads)

print(" - ".join(shortest_path))
print(total_distance)
