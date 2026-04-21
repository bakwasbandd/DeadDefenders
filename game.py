import pygame
from path_finding import a_star, heuristic, get_neighbors



def run_game(screen):
    clock = pygame.time.Clock()

    grid= [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0]
    
    ]

    player = [0,0]
    goal = (4,4)
    zombie = [0,4]
    tile_size = 80

    zombie_delay = 500   #milliseconds (adjust this)
    last_zombie_move = pygame.time.get_ticks()

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

        if current_time - last_zombie_move > zombie_delay:
            
            path = a_star(grid, tuple(zombie), tuple(player))

            if path and len(path) > 1:
                zombie[0], zombie[1] = path[1]

            last_zombie_move = current_time

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
        
        #draw zombie
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

