import pygame
from path_finding import a_star, heuristic, get_neighbors
from grid_generator import generate_smart_grid
import random



def run_game(screen):
    clock = pygame.time.Clock()

    grid, player, goal,zombies=generate_smart_grid(10 , 10)

    player=list(player)
    zombies =[list(z) for z in zombies] 
    tile_size = 50

    # zombie_delay=[150, 200, 300]
    zombie_delays = [950, 700, 600]   # staggered delays
    last_move_times = [pygame.time.get_ticks() for _ in zombies]

    running = True
    while running:
        print("GameLoop running")
        screen.fill((30,30,30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player[1] > 0 and grid[player[1]-1][player[0]] == 0:
                        player[1] -= 1

                if event.key == pygame.K_DOWN:
                    if player[1] < len(grid)-1 and grid[player[1]+1][player[0]] == 0:
                        player[1] += 1

                if event.key == pygame.K_LEFT:
                    if player[0] > 0 and grid[player[1]][player[0]-1] == 0:
                        player[0] -= 1

                if event.key == pygame.K_RIGHT:
                    if player[0] < len(grid[0])-1 and grid[player[1]][player[0]+1] == 0:
                        player[0] += 1

                if tuple(player)==goal:
                    print("Goal Reached")
                    running=False

        #zombie pathfinding

        current_time = pygame.time.get_ticks()

        for i, zombie in enumerate(zombies):

            if current_time - last_move_times[i] > zombie_delays[i]:

                path = a_star(grid, tuple(zombie), tuple(player))

                if path and len(path) > 1:
                    zombie[0], zombie[1] = path[1]

                last_move_times[i] = current_time

        for zombie in zombies:
            if zombie == player:
                print("U dead")
                running=False


        #draw grid
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                color = (200, 200, 200)
                if grid[y][x] == 1:
                    color = (0, 0, 0)

                pygame.draw.rect(
                    screen,
                    color,
                    (x * tile_size, y * tile_size, tile_size, tile_size)
                )
        
        #draw zombies
        for zombie in zombies:
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (zombie[0] * tile_size, zombie[1] * tile_size, tile_size, tile_size)
            )
        #draw player
        pygame.draw.rect(
            screen,
            (0, 0, 255),
            (player[0] * tile_size, player[1] * tile_size, tile_size, tile_size)
        )

        
        #draw goal
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (goal[0] * tile_size, goal[1] * tile_size, tile_size, tile_size)
        )

        pygame.display.update()
        clock.tick(60)

