import pygame
import sys

# --- Init ---
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dead Defenders")

clock = pygame.time.Clock()

# --- Load Background ---
background = pygame.image.load("images\homepage/background.PNG")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# --- Button Class ---
class Button:
    def __init__(self, image_path, x, y, scale=1):
        self.original = pygame.image.load(image_path).convert_alpha()

        w = self.original.get_width()
        h = self.original.get_height()

        self.image = pygame.transform.scale(
            self.original, (int(w * scale), int(h * scale))
        )
        self.rect = self.image.get_rect(topleft=(x, y))

        self.hovered = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if not self.hovered:
                self.hovered = True
                self.image = pygame.transform.scale(
                    self.original,
                    (int(self.rect.width * 1.1), int(self.rect.height * 1.1))
                )
                self.rect = self.image.get_rect(center=self.rect.center)
        else:
            if self.hovered:
                self.hovered = False
                self.image = pygame.transform.scale(
                    self.original,
                    (int(self.rect.width / 1.1), int(self.rect.height / 1.1))
                )
                self.rect = self.image.get_rect(center=self.rect.center)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# --- Create Buttons (RIGHT SIDE STACK) ---
start_btn = Button("images\homepage/start.PNG", WIDTH - 450, 120, 0.2)
about_btn = Button("images\homepage/about.PNG", WIDTH - 450, 220, 0.1)
help_btn = Button("images\homepage/help.PNG", WIDTH - 370, 280, 0.07)
quit_btn = Button("images\homepage/quit.PNG", WIDTH - 370, 370, 0.09)

buttons = [start_btn, about_btn, help_btn, quit_btn]


# --- Main Loop ---
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    # Draw background
    screen.blit(background, (0, 0))

    # Update + Draw buttons
    for btn in buttons:
        btn.update(mouse_pos)
        btn.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_btn.is_clicked(mouse_pos):
                print("START clicked")

            elif about_btn.is_clicked(mouse_pos):
                print("ABOUT clicked")

            elif help_btn.is_clicked(mouse_pos):
                print("HELP clicked")

            elif quit_btn.is_clicked(mouse_pos):
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()