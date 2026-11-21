import pygame
from game_engine import GameEngine

class App:
    DISPLAY_SIZE = 700

    def __init__(self, display_size: int = 700):
        self.DISPLAY_SIZE = display_size
        pygame.init()
        self.screen = pygame.display.set_mode((self.DISPLAY_SIZE, self.DISPLAY_SIZE))
        pygame.display.set_caption("Neural Paper.io")
        self.clock = pygame.Clock()
        self.engine = GameEngine()

    def draw_map(self) -> None:
        self.screen.fill(pygame.Color(31, 139, 201))
        center = (self.DISPLAY_SIZE / 2, self.DISPLAY_SIZE / 2)
        radius = self.DISPLAY_SIZE / 2
        pygame.draw.circle(self.screen, pygame.Color("white"), center, radius)

    def draw_bots(self) -> None:
        for bot in self.engine.bots:
            rect = pygame.rect.Rect(0, 0, bot.size, bot.size)
            rect.center = bot.pos
            pygame.draw.rect(self.screen, bot.color, rect)

    def draw(self) -> None:
        self.draw_map()
        self.draw_bots()

    def main(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            self.engine.step()
            pygame.display.update()
            self.clock.tick(120)

        pygame.quit()