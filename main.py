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

class Button:
    def __init__(self, image_path, x, y, scale=1, angle=0):
        self.original = pygame.image.load(image_path).convert_alpha()

        # Scale first
        w = self.original.get_width()
        h = self.original.get_height()

        scaled = pygame.transform.scale(
            self.original,
            (int(w * scale), int(h * scale))
        )

        # Then rotate
        self.image = pygame.transform.rotate(scaled, angle)

        self.rect = self.image.get_rect(topleft=(x, y))

        self.scale = scale
        self.angle = angle
        self.hovered = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if not self.hovered:
                self.hovered = True
                self._transform(1.1)
        else:
            if self.hovered:
                self.hovered = False
                self._transform(1)

    def _transform(self, hover_scale):
        w = self.original.get_width()
        h = self.original.get_height()

        scaled = pygame.transform.scale(
            self.original,
            (
                int(w * self.scale * hover_scale),
                int(h * self.scale * hover_scale)
            )
        )

        self.image = pygame.transform.rotate(scaled, self.angle)

        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


start_btn = Button("images/homepage/start.PNG", WIDTH - 430, 110, 0.17, -6)
about_btn = Button("images/homepage/about.PNG", WIDTH - 430, 200, 0.085, -9)
help_btn = Button("images/homepage/help.PNG", WIDTH - 400, 290, 0.03, -9)
quit_btn = Button("images/homepage/quit.PNG", WIDTH - 400, 360, 0.09, -9)
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