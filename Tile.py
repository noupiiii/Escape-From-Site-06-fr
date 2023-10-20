import pygame
from Position import Position


class Tile:
    def __init__(self, x: int, y: int, texture: pygame.image, size: int = 32) -> None:
        """
        Initialise un objet Tile qui représente une case de la carte.

        Args:
            x (int): Position en abscisse de la case.
            y (int): Position en ordonnée de la case.
            texture (pygame.image): Texture associée à la case.
            size (int, optional): Taille de la case en pixels. Par défaut, 32.

        Attributes:
            position (Position): Position de la case.
            texture (pygame.image): Texture de la case.
            size (int): Taille de la case en pixels.
            window_center_x (int): Centre de la fenêtre en abscisse.
            window_center_y (int): Centre de la fenêtre en ordonnée.
        """
        self.position = Position(x, y)
        self.texture = texture

        # Rotation de la texture en fonction de la position
        if self.position.x == 22 and self.position.y == 11:
            self.texture = pygame.transform.rotate(self.texture, 90)
        if self.position.x == 16 and self.position.y == 13:
            self.texture = pygame.transform.rotate(self.texture, 180)

        self.size = size

        self.window_center_x = 1920 // 2
        self.window_center_y = 1080 // 2

    def setPosition(self, x: int, y: int):
        """
        Modifie la position de la case.

        Args:
            x (int): Nouvelle position en abscisse.
            y (int): Nouvelle position en ordonnée.
        """
        self.position = Position(x, y)

    def setTexture(self, texture: pygame.image):
        """
        Modifie la texture de la case.

        Args:
            texture (pygame.image): Nouvelle texture de la case.
        """
        self.texture = texture

    def display(self, screen: pygame.display):
        """
        Affiche la case sur l'écran.

        Args:
            screen (pygame.display): Surface d'affichage de pygame.
        """
        # Redimensionne la texture pour correspondre à la taille de la case
        self.texture = pygame.transform.scale(
            self.texture, (self.size, self.size))

        # Calcule les coordonnées d'affichage en fonction de la position et de la taille
        x_pos = (self.position.x - 15) * self.size + self.window_center_x
        y_pos = (self.position.y - 10) * self.size + self.window_center_y

        # Affiche la texture sur l'écran
        screen.blit(self.texture, (x_pos, y_pos))
