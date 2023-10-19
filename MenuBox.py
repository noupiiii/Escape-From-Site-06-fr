import pygame


class MenuBox:
    def __init__(self, screen) -> None:
        self.visible = False
        self.screen = screen

    def display(self):
        if self.visible:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (500, 300, 1300, 700), 1)
