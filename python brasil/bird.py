import pygame
import random

# Configurações do jogo
WIDTH, HEIGHT = 500, 600
PIPE_WIDTH = 50
GRAVITY = 0.25
FLAP_POWER = -7
PIPE_GAP = 200
PIPE_SPEED = 3
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicialização do Pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Classe do pássaro
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.vel = 0
        self.img = pygame.image.load('imagens/bird.png')

    def flap(self):
        self.vel = FLAP_POWER

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel
        if self.y < 0 or self.y > HEIGHT:
            game_over()
        win.blit(self.img, (self.x, self.y))

# Classe do tubo
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.gap = random.randint(150, 300)
        self.top = self.gap - PIPE_GAP // 2
        self.bottom = self.gap + PIPE_GAP // 2

    def update(self):
        self.x -= PIPE_SPEED
        pygame.draw.rect(win, BLACK, (self.x, 0, PIPE_WIDTH, self.top))
        pygame.draw.rect(win, BLACK, (self.x, self.bottom, PIPE_WIDTH, HEIGHT))

# Função de fim de jogo
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, WHITE)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

# Função principal
def main():
    bird = Bird()
    pipes = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        win.fill(WHITE)
        bird.update()

        if len(pipes) == 0 or pipes[-1].x < WIDTH - 200:
            pipes.append(Pipe())

        for pipe in pipes:
            pipe.update()
            if pipe.x < -PIPE_WIDTH:
                pipes.remove(pipe)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()