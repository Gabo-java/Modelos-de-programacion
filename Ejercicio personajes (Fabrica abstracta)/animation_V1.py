# main.py
import pygame

# ---------------------------
# Settings
# ---------------------------
WIDTH, HEIGHT = 800, 400
BG_COLOR = (25, 28, 35)
FPS = 60

LEVEL_WIDTH = 2000  # world width in pixels

RUNNER_COLOR = (80, 200, 120)
RUNNER_W, RUNNER_H = 48, 64
GROUND_Y = HEIGHT // 2 + 80  # world ground line (visual)

TOKEN_SPEED_COLOR = (255, 180, 0)
TOKEN_SHIELD_COLOR = (0, 180, 255)
TOKEN_SIZE = 28

# ---------------------------
# Actor interface and runner
# ---------------------------
class IActor:
    def handle_input(self, keys): ...
    def update(self, dt): ...
    def draw(self, surf, offset): ...
    def get_rect(self): ...
    def speed(self): ...

class Runner(IActor):
    def __init__(self, x):
        self.base_speed = 240.0  # px/s
        self.vx = 0.0
        self.x = float(x)
        self.y = float(GROUND_Y - RUNNER_H)
        self.rect = pygame.Rect(int(self.x), int(self.y), RUNNER_W, RUNNER_H)
        self.color = RUNNER_COLOR

    def speed(self):
        return self.base_speed

    def handle_input(self, keys):
        left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        direction = (-1 if left else 0) + (1 if right else 0)
        self.vx = direction * self.speed()

    def update(self, dt):
        self.x += self.vx * dt
        self.x = max(0, min(self.x, LEVEL_WIDTH - RUNNER_W))
        self.rect.x = int(self.x)
        return self  # return current active actor (may be a decorator chain)

    def draw(self, surf, offset):
        # Convert world rect -> screen rect by subtracting camera offset
        screen_rect = self.rect.move(-offset[0], -offset[1])
        pygame.draw.rect(surf, self.color, screen_rect)

    def get_rect(self):
        return self.rect

# ---------------------------
# Decorator base
# ---------------------------
class ActorDecorator(IActor):
    def __init__(self, wrapped: IActor):
        self.wrapped = wrapped

    def handle_input(self, keys):
        return self.wrapped.handle_input(keys)

    def update(self, dt):
        self.wrapped = self.wrapped.update(dt)
        return self

    def draw(self, surf, offset):
        return self.wrapped.draw(surf, offset)

    def get_rect(self):
        return self.wrapped.get_rect()

    def speed(self):
        return self.wrapped.speed()

# ---------------------------
# Speed boost decorator
# ---------------------------
class SpeedBoost(ActorDecorator):
    def __init__(self, wrapped: IActor, factor=1.6, duration=4.0):
        super().__init__(wrapped)
        self.factor = factor
        self.remaining = duration
        self.overlay_color = (255, 230, 120)

    def speed(self):
        return self.wrapped.speed() * self.factor

    def handle_input(self, keys):
        self.wrapped.handle_input(keys)
        if hasattr(self.wrapped, "vx"):
            base = self.wrapped.vx
            if base != 0:
                direction = 1 if base > 0 else -1
                self.wrapped.vx = direction * self.speed()

    def update(self, dt):
        self.remaining -= dt
        self.wrapped = self.wrapped.update(dt)
        if self.remaining <= 0:
            return self.wrapped
        return self

    def draw(self, surf, offset):
        # Draw wrapped, then overlay aligned in scrolled space
        self.wrapped.draw(surf, offset)
        world_rect = self.get_rect()
        screen_rect = world_rect.move(-offset[0], -offset[1])
        pygame.draw.rect(surf, self.overlay_color, screen_rect, width=3)

# ---------------------------
# Shield decorator
# ---------------------------
class Shield(ActorDecorator):
    def __init__(self, wrapped: IActor, duration=5.0):
        super().__init__(wrapped)
        self.remaining = duration
        self.overlay_color = (140, 220, 255)

    def update(self, dt):
        self.remaining -= dt
        self.wrapped = self.wrapped.update(dt)
        if self.remaining <= 0:
            return self.wrapped
        return self

    def draw(self, surf, offset):
        self.wrapped.draw(surf, offset)
        world_rect = self.get_rect()
        screen_rect = world_rect.move(-offset[0], -offset[1])
        pygame.draw.rect(surf, self.overlay_color, screen_rect.inflate(10, 10), width=2, border_radius=10)

# ---------------------------
# Tokens (collectibles)
# ---------------------------
class Token(pygame.sprite.Sprite):
    def __init__(self, x, y, kind="speed"):
        super().__init__()
        self.kind = kind
        color = TOKEN_SPEED_COLOR if kind == "speed" else TOKEN_SHIELD_COLOR
        self.image = pygame.Surface((TOKEN_SIZE, TOKEN_SIZE), pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

# ---------------------------
# Camera helpers
# ---------------------------
def compute_camera_x(focus_rect, screen_w, world_w):
    # Center camera on focus; clamp to world
    target = focus_rect.centerx - screen_w // 2
    return max(0, min(target, world_w - screen_w))

# ---------------------------
# Game loop
# ---------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Decorator Power-Ups (Scrolling)")
    clock = pygame.time.Clock()

    actor: IActor = Runner(x=WIDTH // 4)

    tokens = pygame.sprite.Group()
    tokens.add(Token(520, GROUND_Y - TOKEN_SIZE - 4, "speed"))
    tokens.add(Token(900, GROUND_Y - TOKEN_SIZE - 4, "shield"))
    tokens.add(Token(1350, GROUND_Y - TOKEN_SIZE - 4, "speed"))

    running = True
    while running:
        dt_ms = clock.tick(FPS)
        dt = dt_ms / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        actor.handle_input(keys)

        # Update actor (decorators may unwrap)
        actor = actor.update(dt)

        # Collisions in world space (no camera offset)
        player_rect = actor.get_rect()
        for token in list(tokens):
            if player_rect.colliderect(token.rect):
                if token.kind == "speed":
                    actor = SpeedBoost(actor, factor=1.6, duration=4.0)
                elif token.kind == "shield":
                    actor = Shield(actor, duration=5.0)
                token.kill()

        # Camera follows actor horizontally
        camera_x = compute_camera_x(actor.get_rect(), WIDTH, LEVEL_WIDTH)
        offset = (camera_x, 0)

        # Draw
        screen.fill(BG_COLOR)

        # World ground line (scrolled)
        pygame.draw.line(
            screen,
            (60, 60, 70),
            (0 - offset[0], GROUND_Y - offset[1]),
            (LEVEL_WIDTH - offset[0], GROUND_Y - offset[1]),
            2,
        )

        # Draw tokens in scrolled space
        for t in tokens:
            screen.blit(t.image, t.rect.move(-offset[0], -offset[1]))

        # Draw actor and overlays with same offset
        actor.draw(screen, offset)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()