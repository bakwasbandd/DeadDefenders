import pygame
import random
from path_finding import a_star
from grid_generator import generate_smart_grid
from end_screen import show_end_screen


def run_game(screen):
    clock = pygame.time.Clock()

    ROWS, COLS = 15, 15
    TILE_SIZE = 50
    MIN_ZOMBIE_DELAY = 500
    MAX_ZOMBIE_DELAY = 700

    # --- Generate Grid (walls included) ---
    grid, start, goal, zombies = generate_smart_grid(ROWS, COLS)

    agent = list(start)
    current_time = pygame.time.get_ticks()
    zombies = [
        {
            "pos": [z[0], z[1]],
            "delay": random.randint(MIN_ZOMBIE_DELAY, MAX_ZOMBIE_DELAY),
            "last_move": current_time,
        }
        for z in zombies
    ]

    # --- Timers ---
    agent_delay = 450   # slower agent ----or faster?? -usaid
    last_agent_move = current_time

    path = []

    def spawn_zombie():
        occupied_positions = {tuple(agent), goal}
        occupied_positions.update(tuple(z["pos"]) for z in zombies)

        available_cells = [
            (x, y)
            for y in range(ROWS)
            for x in range(COLS)
            if grid[y][x] == 0 and (x, y) not in occupied_positions
        ]

        if not available_cells:
            return False

        spawn_x, spawn_y = random.choice(available_cells)
        zombies.append(
            {
                "pos": [spawn_x, spawn_y],
                "delay": random.randint(MIN_ZOMBIE_DELAY, MAX_ZOMBIE_DELAY),
                "last_move": pygame.time.get_ticks(),
            }
        )
        return True

    running = True
    while running:
        screen.fill((30, 30, 30))

        # --- EVENTS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                spawn_zombie()

        current_time = pygame.time.get_ticks()

        # --- TEMP GRID (walls + zombies) ---
        temp_grid = [row[:] for row in grid]
        for z in zombies:
            zx, zy = z["pos"]
            temp_grid[zy][zx] = 1

        # --- A* PATH ---
        path = a_star(temp_grid, tuple(agent), goal)

        # --- MOVE AGENT ---
        if path and len(path) > 1:
            if current_time - last_agent_move > agent_delay:
                agent[0], agent[1] = path[1]
                last_agent_move = current_time

        # --- MOVE ZOMBIES ---
        for z in zombies:
            if current_time - z["last_move"] <= z["delay"]:
                continue

            zx, zy = z["pos"]

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = zx + dx, zy + dy

                if 0 <= nx < COLS and 0 <= ny < ROWS:
                    occupied_by_other_zombie = any(
                        other is not z and other["pos"] == [nx, ny]
                        for other in zombies
                    )

                    if (
                        grid[ny][nx] == 0
                        and (nx, ny) != goal
                        # and [nx, ny] != agent
                        and not occupied_by_other_zombie
                    ):
                        z["pos"] = [nx, ny]
                        break

            z["last_move"] = current_time

        # --- CHECK DEATH ---
        for z in zombies:
            if z["pos"] == agent:
                print("Agent died")

                result = show_end_screen(screen, "GAME OVER\bYOU DIED")

                if result == "retry":
                    return run_game(screen)
                else:
                    return

        # --- CHECK GOAL ---
        if tuple(agent) == goal:
            print("Goal reached!")

            result = show_end_screen(screen, "YOU WIN")

            if result == "retry":
                return run_game(screen)
            else:
                return

        # --- DRAW GRID ---
        for y in range(ROWS):
            for x in range(COLS):
                color = (200, 200, 200)

                if grid[y][x] == 1:
                    color = (0, 0, 0)  # WALL

                pygame.draw.rect(
                    screen,
                    color,
                    (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )

                pygame.draw.rect(
                    screen,
                    (50, 50, 50),
                    (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE),
                    1
                )

        # --- DRAW PATH ---
        if path:
            for node in path:
                pygame.draw.rect(
                    screen,
                    (0, 255, 255),
                    (node[0]*TILE_SIZE, node[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )

        # --- DRAW GOAL ---
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (goal[0]*TILE_SIZE, goal[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )

        # --- DRAW ZOMBIES ---
        for z in zombies:
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (z["pos"][0]*TILE_SIZE, z["pos"][1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            )

        # --- DRAW AGENT ---
        pygame.draw.rect(
            screen,
            (0, 0, 255),
            (agent[0]*TILE_SIZE, agent[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )

        pygame.display.update()
        clock.tick(60)
