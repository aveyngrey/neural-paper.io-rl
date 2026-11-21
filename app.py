import pygame

class App:
    DISPLAY_SIZE = 700

    def __init__(self, display_size: int = 700):
        self.DISPLAY_SIZE = display_size
        pygame.init()
        self.screen = pygame.display.set_mode((self.DISPLAY_SIZE, self.DISPLAY_SIZE))
        pygame.display.set_caption("Neural Paper.io")
        self.clock = pygame.Clock()

    def draw_map(self) -> None:
        self.screen.fill(pygame.Color(31, 139, 201))
        center = (self.DISPLAY_SIZE / 2, self.DISPLAY_SIZE / 2)
        radius = self.DISPLAY_SIZE / 2
        pygame.draw.circle(self.screen, pygame.Color("white"), center, radius)

    def draw(self) -> None:
        self.draw_map()

    def main(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            pygame.display.update()
            self.clock.tick(120)

        pygame.quit()