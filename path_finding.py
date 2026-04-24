
def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(node, grid):
    x, y = node
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # bounds check
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            # wall check
            if grid[ny][nx] == 0:
                neighbors.append((nx, ny))

    return neighbors


def a_star(grid, start, goal):

    frontier = [(start, heuristic(start, goal))]
    visited = set()
    g_costs = {start: 0}
    came_from = {start: None}

    while frontier:
        # Sort by f(n)
        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=" ")
        visited.add(current_node)

        # Goal check
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()

            print(f"\nGoal found. Path: {path}")
            return path

        #generate neighbors from grid
        for neighbor in get_neighbors(current_node, grid):
            new_g_cost = g_costs[current_node] + 1  # uniform cost

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = current_node

                f_cost = new_g_cost + heuristic(neighbor, goal)
                frontier.append((neighbor, f_cost))

    print("\nGoal not found")
    return None


