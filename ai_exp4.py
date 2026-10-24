import heapq

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f(n), g(n), node, path)
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, g, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", g)
            return

        # Explore neighbors
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("Path not found")


# Graph with edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values h(n)
heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

# A* Search
a_star(graph, heuristic, 'A', 'G')