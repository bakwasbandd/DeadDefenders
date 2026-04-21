# import pygame
# import sys


# def run_about_screen(screen):
#     WIDTH, HEIGHT = screen.get_size()
#     clock = pygame.time.Clock()

#     # --- Load Slides ---
#     slides = [
#         pygame.image.load("images/aboutGame/1.PNG").convert_alpha(),
#         pygame.image.load("images/aboutGame/2.PNG").convert_alpha(),
#         pygame.image.load("images/aboutGame/3.PNG").convert_alpha()
#     ]

#     # Scale slides to fit screen nicely
#     slides = [pygame.transform.scale(img, (WIDTH, HEIGHT)) for img in slides]

#     # --- Load Buttons ---
#     next_btn_img = pygame.image.load("images/aboutGame/next.PNG").convert_alpha()
#     home_btn_img = pygame.image.load("images/aboutGame/home.PNG").convert_alpha()

#     next_btn_img = pygame.transform.scale(next_btn_img, (200, 100))
#     home_btn_img = pygame.transform.scale(home_btn_img, (200, 100))

#     next_rect = next_btn_img.get_rect(center=(WIDTH - 120, HEIGHT - 350))
#     home_rect = home_btn_img.get_rect(center=(WIDTH - 120, HEIGHT - 350))

#     current_slide = 0
#     running = True

#     while running:
#         screen.blit(slides[current_slide], (0, 0))

#         # Show NEXT or HOME depending on slide
#         if current_slide < len(slides) - 1:
#             screen.blit(next_btn_img, next_rect)
#         else:
#             screen.blit(home_btn_img, home_rect)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = event.pos

#                 # NEXT button
#                 if current_slide < len(slides) - 1:
#                     if next_rect.collidepoint(mouse_pos):
#                         current_slide += 1

#                 # HOME button (last slide)
#                 else:
#                     if home_rect.collidepoint(mouse_pos):
#                         return  # exit back to main.py

#         pygame.display.update()
#         clock.tick(60)

import pygame
import sys


def fade(screen, from_surf, to_surf, duration=300):
    clock = pygame.time.Clock()
    alpha = 0

    fade_surface = to_surf.copy()
    fade_surface.set_alpha(alpha)

    while alpha < 255:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        alpha += 255 / (duration / 16)  # smooth timing
        if alpha > 255:
            alpha = 255

        screen.blit(from_surf, (0, 0))
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))

        pygame.display.update()
        clock.tick(60)


def run_about_screen(screen):
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()

    # --- Load Slides ---
    slides = [
        pygame.image.load("images/aboutGame/1.PNG").convert_alpha(),
        pygame.image.load("images/aboutGame/2.PNG").convert_alpha(),
        pygame.image.load("images/aboutGame/3.PNG").convert_alpha()
    ]

    slides = [pygame.transform.scale(img, (WIDTH, HEIGHT)) for img in slides]

    # --- Buttons ---
    next_img = pygame.image.load("images/aboutGame/next.PNG").convert_alpha()
    home_img = pygame.image.load("images/aboutGame/home.PNG").convert_alpha()

    next_img = pygame.transform.scale(next_img, (200, 100))
    home_img = pygame.transform.scale(home_img, (200, 100))

    next_rect = next_img.get_rect(center=(WIDTH - 120, HEIGHT - 350))
    home_rect = home_img.get_rect(center=(WIDTH - 120, HEIGHT - 350))

    current_slide = 0
    running = True

    while running:
        screen.blit(slides[current_slide], (0, 0))

        # Draw correct button
        if current_slide < len(slides) - 1:
            screen.blit(next_img, next_rect)
        else:
            screen.blit(home_img, home_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # NEXT
                if current_slide < len(slides) - 1:
                    if next_rect.collidepoint(mouse_pos):
                        next_slide = current_slide + 1

                        # Fade transition
                        fade(screen, slides[current_slide], slides[next_slide])

                        current_slide = next_slide

                # HOME
                else:
                    if home_rect.collidepoint(mouse_pos):
                        return

        pygame.display.update()
        clock.tick(60)