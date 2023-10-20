import pygame
import random as rd
from Player import Player


class GestionDes:
    def __init__(self) -> None:
        """Constructeur de la classe GestionDes. Initialise la police de caractères et la valeur aléatoire du dé.

        Attributes:
            font (str): Le chemin de la police de caractères utilisée.
            random_value: La valeur aléatoire du dé.
        """
        self.font = "assets/fonts/iknowaghost.ttf"
        self.random_value = None

    def set_random_value(self, random_value):
        """Définit la valeur aléatoire du dé.

        Args:
            random_value: La valeur aléatoire du dé à définir.
        """
        self.random_value = random_value

    def display_rect(self, screen: pygame.display):
        """Affiche un rectangle sur l'écran.

        Args:
            screen (pygame.display): La surface d'affichage où le rectangle doit être affiché.
        """
        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect(10, 1080 // 2 - 37.5, 75, 75), 3)

    def display_number(self, screen: pygame.display, current_player: Player):
        """Affiche la valeur du dé et le nombre de coups restants sur l'écran.

        Args:
            screen (pygame.display): La surface d'affichage où les informations doivent être affichées.
            current_player (Player): Le joueur actuel.
        """
        font = pygame.font.Font(self.font, 75)
        texte_surface = font.render(
            str(self.random_value), True, (255, 127, 0))

        # Centre le texte dans le rectangle d'affichage
        texte_rect = texte_surface.get_rect()
        texte_rect.center = (10 + 75 / 2, 1080 // 2)

        screen.blit(texte_surface, texte_rect.topleft)

        font = pygame.font.Font(self.font, 25)
        texte_surface = font.render("total", True, (255, 128, 0))
        texte_rect = texte_surface.get_rect()
        texte_rect.center = (10 + 75 / 2, 1080 // 2 - 75)
        screen.blit(texte_surface, texte_rect)

        # Affiche le nombre de coups restants.
        restant = self.random_value - current_player.move_count

        font = pygame.font.Font(self.font, 75)
        texte_surface = font.render(
            str(restant), True, (255, 255, 255))

        # Centre le texte dans le rectangle d'affichage
        texte_rect = texte_surface.get_rect()
        texte_rect.center = ((10 + 75 / 2) + 100, 1080 // 2)

        screen.blit(texte_surface, texte_rect.topleft)

        font = pygame.font.Font(self.font, 25)
        texte_surface = font.render("remaining", True, (255, 255, 255))
        texte_rect = texte_surface.get_rect()
        texte_rect.center = ((10 + 75 / 2) + 100, 1080 // 2 - 75)
        screen.blit(texte_surface, texte_rect)

    def lancer_de(self):
        """Lance le dé en attribuant une valeur aléatoire à `random_value` (de 1 à 6)."""
        self.set_random_value(rd.randint(1, 6))

    def display(self, screen: pygame.display, current_player: Player):
        """Affiche le rectangle, la valeur du dé et le nombre de coups restants.

        Args:
            screen (pygame.display): La surface d'affichage où les informations doivent être affichées.
            current_player (Player): Le joueur actuel.
        """
        self.display_rect(screen)
        self.display_number(screen, current_player)
