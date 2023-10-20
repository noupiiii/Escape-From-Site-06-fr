import pygame


class MenuBox:
    """Cette classe gère l'affichage d'une boîte de menu.

    La boîte de menu est un rectangle qui peut être affiché ou masqué sur l'écran du jeu.

    Attributes:
        visible (bool): Indique si la boîte de menu est visible ou masquée.
        screen: La surface d'affichage du jeu.

    Methods:
        display(): Affiche la boîte de menu sur l'écran.
    """

    def __init__(self, screen) -> None:
        """Initialise la boîte de menu.

        Args:
            screen: La surface de l'écran du jeu.
        """
        self.visible = False
        self.screen = screen

    def display(self):
        """Affiche la boîte de menu sur l'écran.

        La boîte de menu est un rectangle avec une bordure blanche.
        """
        if self.visible:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (500, 300, 1300, 700), 1)
