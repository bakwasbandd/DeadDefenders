import pygame
import random
from path_finding import a_star
from grid_generator import generate_smart_grid
from end_screen import show_end_screen


# --- Collision Pause ---
def show_collision_pause(screen, agent_pos, TILE_SIZE):
    overlay = pygame.Surface(screen.get_size())
    overlay.set_alpha(120)
    overlay.fill((0, 0, 0))

    pygame.draw.rect(
        screen,
        (255, 255, 0),
        (agent_pos[0]*TILE_SIZE, agent_pos[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
    )

    screen.blit(overlay, (0, 0))
    pygame.display.update()
    pygame.time.delay(800)


def run_game(screen):
    clock = pygame.time.Clock()

    ROWS, COLS = 15, 15
    TILE_SIZE = 55

    MIN_ZOMBIE_DELAY = 500
    MAX_ZOMBIE_DELAY = 700

    # --- Spawn cooldown ---
    zombie_spawn_cooldown = 5000
    last_spawn_time = 0

    # --- Generate Grid ---
    grid, _, _, zombies = generate_smart_grid(ROWS, COLS)

    placing_mode = True
    start = None
    goal = None
    agent = None

    current_time = pygame.time.get_ticks()

    zombies = [
        {
            "pos": [z[0], z[1]],
            "delay": random.randint(MIN_ZOMBIE_DELAY, MAX_ZOMBIE_DELAY),
            "last_move": current_time,
        }
        for z in zombies
    ]

    agent_delay = 500
    last_agent_move = current_time

    path = []

    running = True
    while running:
        screen.fill((30, 30, 30))
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        # ================= EVENTS =================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = mouse_pos[0] // TILE_SIZE
                y = mouse_pos[1] // TILE_SIZE

                if 0 <= x < COLS and 0 <= y < ROWS:

                    if placing_mode:
                        if grid[y][x] == 0:
                            if keys[pygame.K_s]:
                                start = (x, y)

                            elif keys[pygame.K_g]:
                                goal = (x, y)

                    else:
                        if keys[pygame.K_z]:
                            if current_time - last_spawn_time >= zombie_spawn_cooldown:

                                occupied = {tuple(agent), goal}
                                occupied.update(tuple(z["pos"]) for z in zombies)

                                if grid[y][x] == 0 and (x, y) not in occupied:
                                    zombies.append({
                                        "pos": [x, y],
                                        "delay": random.randint(MIN_ZOMBIE_DELAY, MAX_ZOMBIE_DELAY),
                                        "last_move": pygame.time.get_ticks(),
                                    })
                                    last_spawn_time = current_time

            if event.type == pygame.KEYDOWN:
                if placing_mode and event.key == pygame.K_RETURN:
                    if start and goal:
                        agent = list(start)
                        placing_mode = False

        current_time = pygame.time.get_ticks()

        # ================= TEMP GRID =================
        temp_grid = [row[:] for row in grid]
        for z in zombies:
            zx, zy = z["pos"]
            temp_grid[zy][zx] = 1

        # ================= PATH =================
        if not placing_mode and start and goal:
            path = a_star(temp_grid, tuple(agent), goal)
        else:
            path = []

        # ================= MOVE AGENT =================
        if not placing_mode and path and len(path) > 1:
            if current_time - last_agent_move > agent_delay:
                agent[0], agent[1] = path[1]
                last_agent_move = current_time

        # ================= MOVE ZOMBIES =================
        if not placing_mode:
            for z in zombies:
                if current_time - z["last_move"] <= z["delay"]:
                    continue

                zx, zy = z["pos"]
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                random.shuffle(directions)

                for dx, dy in directions:
                    nx, ny = zx + dx, zy + dy

                    if 0 <= nx < COLS and 0 <= ny < ROWS:
                        occupied = any(
                            other is not z and other["pos"] == [nx, ny]
                            for other in zombies
                        )

                        if grid[ny][nx] == 0 and (nx, ny) != goal and not occupied:
                            z["pos"] = [nx, ny]
                            break

                z["last_move"] = current_time

        # ================= CHECK COLLISION =================
        if not placing_mode:
            for z in zombies:
                if z["pos"] == agent:
                    show_collision_pause(screen, agent, TILE_SIZE)
                    result = show_end_screen(screen, "GAME OVER")
                    return run_game(screen) if result == "retry" else None

            if tuple(agent) == goal:
                pygame.time.delay(600)
                result = show_end_screen(screen, "YOU WIN")
                return run_game(screen) if result == "retry" else None

        # ================= DRAW GRID =================
        for y in range(ROWS):
            for x in range(COLS):
                color = (200, 200, 200)
                if grid[y][x] == 1:
                    color = (0, 0, 0)

                pygame.draw.rect(screen, color,
                                 (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, (50,50,50),
                                 (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

        # ================= DRAW PATH =================
        if path:
            for node in path:
                pygame.draw.rect(screen, (0,255,255),
                                 (node[0]*TILE_SIZE, node[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

        # ================= DRAW START / GOAL =================
        if start:
            pygame.draw.rect(screen, (0,0,255),
                             (start[0]*TILE_SIZE, start[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

        if goal:
            pygame.draw.rect(screen, (0,255,0),
                             (goal[0]*TILE_SIZE, goal[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

        # ================= DRAW ZOMBIES =================
        for z in zombies:
            pygame.draw.rect(screen, (255,0,0),
                             (z["pos"][0]*TILE_SIZE, z["pos"][1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

        # ================= DRAW AGENT =================
        if agent:
            pygame.draw.rect(screen, (255,255,0),
                             (agent[0]*TILE_SIZE, agent[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

        pygame.display.update()
        clock.tick(60)