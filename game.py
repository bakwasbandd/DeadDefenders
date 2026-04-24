import pygame
import random
from path_finding import a_star
from grid_generator import generate_smart_grid


def show_end_screen(screen, text):
    font = pygame.font.SysFont(None, 72)

    overlay = pygame.Surface(screen.get_size())
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))

    label = font.render(text, True, (255, 255, 255))
    rect = label.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    screen.blit(overlay, (0, 0))
    screen.blit(label, rect)
    pygame.display.update()

    pygame.time.delay(3000)  # 3 sec pause


def run_game(screen):
    clock = pygame.time.Clock()

    ROWS, COLS = 10, 10
    TILE_SIZE = 50

    # --- Grid ---
    grid, start, goal, zombies = generate_smart_grid(ROWS, COLS)

    agent = list(start)
    zombies = [list(z) for z in zombies]

    # --- Timers ---
    zombie_delay = 700
    last_zombie_move = pygame.time.get_ticks()

    # 🔻 SLOWER AGENT HERE
    agent_delay = 400
    last_agent_move = pygame.time.get_ticks()

    path = []

    running = True
    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        current_time = pygame.time.get_ticks()

        # --- Temp Grid ---
        temp_grid = [row[:] for row in grid]
        for z in zombies:
            temp_grid[z[1]][z[0]] = 1

        # --- A* ---
        path = a_star(temp_grid, tuple(agent), goal)

        # --- Move Agent ---
        if path and len(path) > 1:
            if current_time - last_agent_move > agent_delay:
                agent[0], agent[1] = path[1]
                last_agent_move = current_time

        # --- Move Zombies ---
        if current_time - last_zombie_move > zombie_delay:
            for z in zombies:
                zx, zy = z

                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                random.shuffle(directions)

                for dx, dy in directions:
                    nx, ny = zx + dx, zy + dy

                    if 0 <= nx < COLS and 0 <= ny < ROWS:
                        if grid[ny][nx] == 0 and (nx, ny) != goal:
                            z[0], z[1] = nx, ny
                            break

            last_zombie_move = current_time

        # --- CHECK DEATH ---
        for z in zombies:
            if z == agent:
                print("Agent died")
                show_end_screen(screen, "GAME OVER")
                return

        # --- CHECK GOAL ---
        if tuple(agent) == goal:
            print("Goal reached!")
            show_end_screen(screen, "YOU WIN")
            return

        # --- DRAW GRID ---
        for y in range(ROWS):
            for x in range(COLS):
                color = (200, 200, 200)
                if grid[y][x] == 1:
                    color = (0, 0, 0)

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

        # --- GOAL ---
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (goal[0]*TILE_SIZE, goal[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )

        # --- ZOMBIES ---
        for z in zombies:
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (z[0]*TILE_SIZE, z[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            )

        # --- AGENT ---
        pygame.draw.rect(
            screen,
            (0, 0, 255),
            (agent[0]*TILE_SIZE, agent[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )

        pygame.display.update()
        clock.tick(60)