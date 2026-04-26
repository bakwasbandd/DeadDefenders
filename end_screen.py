import pygame


class ImageButton:
    def __init__(self, image_path, x, y, scale=1):
        self.original = pygame.image.load(image_path).convert_alpha()

        w, h = self.original.get_size()
        self.image = pygame.transform.smoothscale(
            self.original,
            (int(w * scale), int(h * scale))
        )

        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


def show_end_screen(screen, result):
    clock = pygame.time.Clock()
    WIDTH, HEIGHT = screen.get_size()

    # ================= BACKGROUND =================
    is_win = "WIN" in result

    if is_win:
        bg = pygame.image.load("images/end_screen/win.png").convert()
    else:
        bg = pygame.image.load("images/end_screen/loser.png").convert()

    # --- Maintain aspect ratio ---
    img_w, img_h = bg.get_size()
    scale = min(WIDTH / img_w, HEIGHT / img_h)

    new_size = (int(img_w * scale), int(img_h * scale))
    bg = pygame.transform.smoothscale(bg, new_size)

    # --- Center properly ---
    bg_rect = bg.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # ================= BUTTON POSITIONS =================
    center_x = WIDTH // 2
    button_y = HEIGHT - 140

    home_btn = ImageButton(
        "images/end_screen/buttons/home.png",
        center_x + 150,
        button_y - 20,
        0.3
    )

    retry_btn = None
    if not is_win:
        retry_btn = ImageButton(
            "images/end_screen/buttons/retry.png",
            center_x - 350,
            button_y - 20,
            0.3
        )

    # ================= LOOP =================
    while True:
        # Clear screen first (prevents visual shifting issues)
        screen.fill((10, 10, 10))

        # Draw centered background
        screen.blit(bg, bg_rect)

        mouse_pos = pygame.mouse.get_pos()

        # Draw buttons
        if retry_btn:
            retry_btn.draw(screen)

        home_btn.draw(screen)

        # ================= EVENTS =================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "home"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if home_btn.is_clicked(mouse_pos):
                    return "home"

                if retry_btn and retry_btn.is_clicked(mouse_pos):
                    return "retry"

        pygame.display.update()
        clock.tick(60)