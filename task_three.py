import heapq


def dijkstra(graph, start):
    dist = {vertex: float('inf') for vertex in graph}
    dist[start] = 0

    parent = {vertex: None for vertex in graph}

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = dist[u] + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(priority_queue, (new_dist, v))

    return dist, parent


def get_path(parent, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    if path[0] == start:
        return path
    return []


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': []
}


start_vertex = 'A'
distances, parents = dijkstra(graph, start_vertex)

print("Найкоротші відстані від вершини", start_vertex)
for vertex in distances:
    print(f"{start_vertex} -> {vertex}: {distances[vertex]}")

print("Шлях A -> F:", get_path(parents, 'A', 'F'))
