import pygame
import sys


class ImageButton:
    def __init__(self, image_path, center_pos, size):
        image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(image, size)
        self.rect = self.image.get_rect(center=center_pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = word if not current_line else f"{current_line} {word}"
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines


def run_help_screen(screen):
    width, height = screen.get_size()
    clock = pygame.time.Clock()
    background_color = (150, 114, 72)
    text_color = (70, 42, 18)

    scroll = pygame.image.load("images/scroll.png").convert_alpha()
    scroll_size = (int(width * 4), int(height * 0.84))
    scroll = pygame.transform.smoothscale(scroll, scroll_size)
    scroll_rect = scroll.get_rect(center=(width // 2, height // 2))

    title_font = pygame.font.SysFont("georgia", 30, bold=True)
    body_font = pygame.font.SysFont("georgia", 20)

    help_lines = [
        "Place start: hold S and click an empty tile.",
        "Place goal: hold G and click an empty tile.",
        "Press Enter after both are set to begin.",
        "Add zombies: hold Z and click empty tiles.",
        "Zombie spawn cooldown: 5000 ms between spawns.",
        "Reach goal to win. Touch a zombie and lose."
    ]

    back_button = ImageButton(
        "images/aboutGame/home.png",
        (500, height - 60),
        (180, 90)
    )

    while True:
        screen.fill(background_color)
        screen.blit(scroll, scroll_rect)

        title_surface = title_font.render("How To Play", True, text_color)
        title_rect = title_surface.get_rect(
            center=(scroll_rect.centerx, scroll_rect.top + 110)
        )
        screen.blit(title_surface, title_rect)

        # text_left = scroll_rect.left + 280
        text_left = width // 2 - 200
        text_top = scroll_rect.top + 150
        text_width = max(220, scroll_rect.width - 560)
        line_gap = 7
        bullet_gap = 12
        current_y = text_top

        for bullet in help_lines:
            wrapped_lines = wrap_text(f"- {bullet}", body_font, text_width)
            for line in wrapped_lines:
                line_surface = body_font.render(line, True, text_color)
                screen.blit(line_surface, (text_left, current_y))
                current_y += body_font.get_linesize() + line_gap
            current_y += bullet_gap

        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    return

        pygame.display.update()
        clock.tick(60)
