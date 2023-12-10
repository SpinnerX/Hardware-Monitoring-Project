import pygame

class Window:
    def __init__(self, title: str, w: int, h: int) -> None:
        self.width = w
        self.height = h
        self.title = title
        self.screen = pygame.display.set_mode((w, h))
        self.surface = pygame.Surface((w, h))
        pygame.display.set_caption(title)
        pygame.display.flip()
        self.isRunning = True
        self.screen.blit(self.surface, (0, 0))
        self.FPS = 60
        self.timestep = pygame.time.Clock()

    # Setting the color
    def setColor(self, color):
        self.screen.fill(color)

    def update(self):
        pygame.display.update()

    # Running the mainloop
    def mainloop(self):
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
            
            self.update()
            self.timestep.tick(self.FPS)

