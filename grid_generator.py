import random
from path_finding import a_star

def generate_smart_grid(rows, cols, num_zombies=3, wall_prob=0.3):
    while True:
        grid = [
            [1 if random.random() < wall_prob else 0 for x in range(cols)]
            for y in range(rows)
        ]

        empty_cells = [
            (x, y)
            for y in range(rows)
            for x in range(cols)
            if grid[y][x] == 0
        ]

        if len(empty_cells) < (rows * cols * 0.4):
            continue

        player = (0,0)
        goal = random.choice(empty_cells)

        zombies = random.sample(empty_cells, num_zombies)

        # ensure all unique
        if player in zombies or goal in zombies:
            continue

        # validate paths
        if not a_star(grid, player, goal):
            continue

        valid = True
        for z in zombies:
            if not a_star(grid, z, player):
                valid = False
                break

        if valid:
            return grid, player, goal, zombies