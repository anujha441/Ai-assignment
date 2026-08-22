import heapq

def best_first_search(graph, heuristic, start, goal):
    visited = set()
    priority_queue = [(heuristic[start], start)]
    path = []

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        path.append(current)

        if current == goal:
            print("Path found:", " -> ".join(path))
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    print("Path not found")


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 7,
    'E': 3,
    'F': 1,
    'G': 0
}

# Best First Search
best_first_search(graph, heuristic, 'A', 'G')