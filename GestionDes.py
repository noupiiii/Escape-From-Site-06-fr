import pygame
import random as rd

from Player import Player


class GestionDes:
    def __init__(self) -> None:
        self.font = "assets/fonts/iknowaghost.ttf"
        self.random_value = None

    def set_random_value(self, random_value):
        self.random_value = random_value

    def display_rect(self, screen: pygame.display):
        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect(10, 1080 // 2 - 37.5, 75, 75), 3)

    def display_number(self, screen: pygame.display, current_player: Player):
        font = pygame.font.Font(self.font, 75)
        texte_surface = font.render(
            str(self.random_value), True, (255, 127, 0))

        # Center the text within the display_rect
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

        # Center the text within the display_rect
        texte_rect = texte_surface.get_rect()
        texte_rect.center = ((10 + 75 / 2) + 100, 1080 // 2)

        screen.blit(texte_surface, texte_rect.topleft)

        font = pygame.font.Font(self.font, 25)
        texte_surface = font.render("remaining", True, (255, 255, 255))
        texte_rect = texte_surface.get_rect()
        texte_rect.center = ((10 + 75 / 2)+100, 1080 // 2 - 75)
        screen.blit(texte_surface, texte_rect)

    def lancer_de(self):
        self.set_random_value(rd.randint(1, 6))

    def display(self, screen: pygame.display, current_player: Player):
        self.display_rect(screen)
        self.display_number(screen, current_player)
