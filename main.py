import pygame
import sys

# --- Init ---
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🧟‍♀️ Dead Defenders 🧟‍♀️")

# --- Load Images ---
background = pygame.image.load("images\homepage/background.PNG")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# start_img = pygame.image.load("assets/start_btn.png").convert_alpha()
# quit_img = pygame.image.load("assets/quit_btn.png").convert_alpha()

# # Resize buttons (adjust if needed)
# start_img = pygame.transform.scale(start_img, (200, 80))
# quit_img = pygame.transform.scale(quit_img, (200, 80))


# --- Button Class ---
class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# # --- Create Buttons (RIGHT SIDE) ---
# start_button = Button(start_img, WIDTH - 250, 200)
# quit_button = Button(quit_img, WIDTH - 250, 320)


# --- Main Loop ---
running = True
while running:
    screen.blit(background, (0, 0))

    # # Draw buttons
    # start_button.draw(screen)
    # quit_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if start_button.is_clicked(event.pos):
        #         print("Start Game Clicked")  # later → switch to game state

        #     if quit_button.is_clicked(event.pos):
                # pygame.quit()
                # sys.exit()

    pygame.display.update()

pygame.quit()
sys.exit()