import pygame
import os
import random

class UIRenderer:
    def __init__(self, tile_size):
        self.TILE_SIZE = tile_size

        # --- Load Agent Sprite ---
        self.agent_img = pygame.image.load("images/agent/lul.png").convert_alpha()
        self.agent_img = pygame.transform.scale(
            self.agent_img, (tile_size, tile_size)
        )

        # --- Load Zombie Sprites ---
        self.zombie_images = []
        zombie_folder = "images/zombies"

        for file in os.listdir(zombie_folder):
            if file.endswith(".png"):
                img = pygame.image.load(
                    os.path.join(zombie_folder, file)
                ).convert_alpha()
                img = pygame.transform.scale(img, (tile_size, tile_size))
                self.zombie_images.append(img)

    def get_random_zombie_sprite(self):
        return random.choice(self.zombie_images)

    # ================= DRAW FUNCTIONS =================

    def draw_grid(self, screen, grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                color = (200, 200, 200)
                if grid[y][x] == 1:
                    color = (0, 0, 0)

                pygame.draw.rect(
                    screen,
                    color,
                    (x*self.TILE_SIZE, y*self.TILE_SIZE,
                     self.TILE_SIZE, self.TILE_SIZE)
                )

                pygame.draw.rect(
                    screen,
                    (50, 50, 50),
                    (x*self.TILE_SIZE, y*self.TILE_SIZE,
                     self.TILE_SIZE, self.TILE_SIZE),
                    1
                )

    def draw_path(self, screen, path):
        for node in path:
            pygame.draw.rect(
                screen,
                (0, 255, 255),
                (node[0]*self.TILE_SIZE,
                 node[1]*self.TILE_SIZE,
                 self.TILE_SIZE, self.TILE_SIZE)
            )

    def draw_start_goal(self, screen, start, goal):
        if start:
            pygame.draw.rect(
                screen,
                (0, 0, 255),
                (start[0]*self.TILE_SIZE,
                 start[1]*self.TILE_SIZE,
                 self.TILE_SIZE, self.TILE_SIZE)
            )

        if goal:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (goal[0]*self.TILE_SIZE,
                 goal[1]*self.TILE_SIZE,
                 self.TILE_SIZE, self.TILE_SIZE)
            )

    def draw_agent(self, screen, agent):
        if agent:
            screen.blit(
                self.agent_img,
                (agent[0]*self.TILE_SIZE,
                 agent[1]*self.TILE_SIZE)
            )

    def draw_zombies(self, screen, zombies):
        for z in zombies:
            screen.blit(
                z["sprite"],
                (z["pos"][0]*self.TILE_SIZE,
                 z["pos"][1]*self.TILE_SIZE)
            )