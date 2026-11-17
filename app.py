import pygame

class App:
    def __init__(self, display_size: int = 700):
        DISPLAY_SIZE = display_size

        pygame.init()
        self.screen = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
        pygame.display.set_caption("Neural Paper.io")
        self.clock = pygame.Clock()

    def main(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(pygame.Color("white"))
            pygame.display.update()
            self.clock.tick(120)

        pygame.quit()