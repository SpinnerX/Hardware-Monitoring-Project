import pygame
from interfaces.widgets.Button import *

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
        cyanColor = pygame.Color(224, 255, 255) # Light cyan
        self.testButton = Button(cyanColor, x=1050, y=150, width=130, height=50, text="New Maze")

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
            
            self.testButton.draw(self.screen)
            self.update()
            self.timestep.tick(self.FPS)

