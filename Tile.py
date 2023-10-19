import pygame
from Position import Position


class Tile:
    def __init__(self, x: int, y: int, texture: pygame.image, size: int = 32) -> None:
        self.position = Position(x, y)
        self.texture = texture
        if self.position.x == 22 and self.position.y == 11:
            self.texture = pygame.transform.rotate(self.texture, 90)
        if self.position.x == 16 and self.position.y == 13:
            self.texture = pygame.transform.rotate(self.texture, 180)

        self.size = size

        self.window_center_x = 1920 // 2
        self.window_center_y = 1080 // 2

    def setPosition(self, x: int, y: int):
        self.position = Position(x, y)

    def setTexture(self, texture: pygame.image):
        self.texture = texture

    def display(self, screen: pygame.display):
        self.texture = pygame.transform.scale(
            self.texture, (self.size, self.size))
        x_pos = (self.position.x - 15) * self.size + self.window_center_x
        y_pos = (self.position.y - 10) * self.size + self.window_center_y
        screen.blit(self.texture, (x_pos, y_pos))
