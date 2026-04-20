import pygame
import sys

# --- Config ---
WIDTH = 600
HEIGHT = 650   # extra space for UI text
ROWS = 20
COLS = 20
CELL_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)   # Start
RED = (200, 0, 0)     # Goal
BLUE = (50, 50, 255)  # UI text

# --- Initialize ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dead Defenders - Phase 2")
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 60)

# --- Grid Data ---
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

start_pos = None
goal_pos = None

# --- Game State ---
MENU = 0
PLAYING = 1
state = MENU


# --- Functions ---
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            color = WHITE

            if grid[row][col] == 1:
                color = BLACK

            if start_pos == (row, col):
                color = GREEN

            if goal_pos == (row, col):
                color = RED

            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRAY, (x, y, CELL_SIZE, CELL_SIZE), 1)


def get_cell_pos(mouse_pos):
    x, y = mouse_pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col


def draw_ui():
    text = font.render("S: Start | G: Goal | Click: Wall | SPACE: Menu", True, BLUE)
    screen.blit(text, (10, HEIGHT - 40))


def draw_menu():
    screen.fill(WHITE)

    title = big_font.render("Dead Defenders", True, BLACK)
    subtitle = font.render("Press SPACE to Start", True, BLUE)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()


# --- Main Loop ---
running = True
while running:

    if state == MENU:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = PLAYING

        continue

    # --- Game Screen ---
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_cell_pos(pos)

        if 0 <= row < ROWS and 0 <= col < COLS:

            # Place START
            if keys[pygame.K_s]:
                start_pos = (row, col)

            # Place GOAL
            elif keys[pygame.K_g]:
                goal_pos = (row, col)

            # Toggle WALL
            else:
                if (row, col) != start_pos and (row, col) != goal_pos:
                    grid[row][col] = 1 if grid[row][col] == 0 else 0

    # Draw everything
    draw_grid()
    draw_ui()

    pygame.display.flip()

pygame.quit()
sys.exit()