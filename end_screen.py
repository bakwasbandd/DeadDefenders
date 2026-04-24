import pygame
import sys


def show_end_screen(screen, text):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 72)
    btn_font = pygame.font.SysFont(None, 40)

    WIDTH, HEIGHT = screen.get_size()

    # Overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))

    # Title
    label = font.render(text, True, (255, 255, 255))
    label_rect = label.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    # Buttons
    retry_text = btn_font.render("RETRY", True, (255, 255, 255))
    home_text = btn_font.render("HOME", True, (255, 255, 255))

    retry_rect = pygame.Rect(WIDTH//2 - 120, HEIGHT//2, 100, 50)
    home_rect = pygame.Rect(WIDTH//2 + 20, HEIGHT//2, 100, 50)

    while True:
        screen.blit(overlay, (0, 0))
        screen.blit(label, label_rect)

        pygame.draw.rect(screen, (0, 150, 0), retry_rect)
        pygame.draw.rect(screen, (150, 0, 0), home_rect)

        screen.blit(retry_text, retry_text.get_rect(center=retry_rect.center))
        screen.blit(home_text, home_text.get_rect(center=home_rect.center))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    return "retry"

                if home_rect.collidepoint(event.pos):
                    return "home"

        pygame.display.update()
        clock.tick(60)