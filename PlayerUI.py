import pygame
from Player import Player
from Players import Players
from Textures import Textures


class PlayerUI:
    def __init__(self, textures: Textures) -> None:
        """
        Initialise une interface utilisateur pour afficher les informations des joueurs.

        Args:
            textures (Textures): Les textures utilisées pour l'interface.
        """
        self.font = "assets/fonts/iknowaghost.ttf"
        self.font = pygame.font.Font(self.font, 20)
        self.gunTexture = textures.textures["gun"]

    def setUI1(self, screen, players: Players):
        """
        Affiche l'interface utilisateur pour le joueur 1.

        Args:
            screen (pygame.display): La surface pygame sur laquelle afficher l'interface.
            players (Players): La classe contenant les joueurs.
        """
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            15, 15, 150, 100), 2, 0, 0, 0, 0, 35)

        texte_surface_fname = self.font.render(
            "Abigail", True, (255, 127, 0))

        texte_rect = texte_surface_fname.get_rect()
        texte_rect.center = (10, 10)

        screen.blit(texte_surface_fname, (30, 25))

        texte_surface_lastName = self.font.render(
            "Briarton", True, (255, 127, 0))

        texte_rect = texte_surface_lastName.get_rect()
        texte_rect.center = (10, 10)

        screen.blit(texte_surface_lastName, (30, 50))

        if players.players[0].gun:
            screen.blit(self.gunTexture, (20, 55))

    def setUI2(self, screen, players: Players):
        """
        Affiche l'interface utilisateur pour le joueur 2.

        Args:
            screen (pygame.display): La surface pygame sur laquelle afficher l'interface.
            players (Players): La classe contenant les joueurs.
        """
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            15, 1080-115, 150, 100), 2, 0, 0, 35)

        texte_surface = self.font.render("Marlton", True, (255, 127, 0))

        texte_rect = texte_surface.get_rect()
        texte_rect.center = (10, 10)

        screen.blit(texte_surface, (30, 1080-75))

        texte_surface = self.font.render("Johnson", True, (255, 127, 0))

        texte_rect = texte_surface.get_rect()
        texte_rect.center = (10, 10)

        screen.blit(texte_surface, (30, 1080-50))

        if players.players[1].gun:
            screen.blit(self.gunTexture, (20, 1080-125))

    def setUI4(self, screen, players: Players):
        """
        Affiche l'interface utilisateur pour le joueur 4.

        Args:
            screen (pygame.display): La surface pygame sur laquelle afficher l'interface.
            players (Players): La classe contenant les joueurs.
        """
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            1920-165, 1080-115, 150, 100), 2, 0, 35)

        texte_surface = self.font.render("Edward", True, (255, 127, 0))

        texte_rect = texte_surface.get_rect()
        texte_rect.center = (10, 10)

        screen.blit(texte_surface, (1920-100, 1080-75))

        texte_surface = self.font.render("Richtofen", True, (255, 127, 0))

        texte_rect = texte_surface.get_rect()
        texte_rect.center = (10, 10)

        screen.blit(texte_surface, (1920-120, 1080-50))

        if players.players[3].gun:
            screen.blit(self.gunTexture, (1920-90, 1080-125))

    def setUI3(self, screen, players: Players):
        """
        Affiche l'interface utilisateur pour le joueur 3.

        Args:
            screen (pygame.display): La surface pygame sur laquelle afficher l'interface.
            players (Players): La classe contenant les joueurs.
        """
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            1920-165, 15, 150, 100), 2, 0, 0, 0, 35)

        texte_surface = self.font.render("Samantah", True, (255, 127, 0))

        texte_rect = texte_surface.get_rect()
        texte_rect.center = (10, 10)

        screen.blit(texte_surface, (1920-120, 25))

        texte_surface = self.font.render("Maxis", True, (255, 127, 0))

        texte_rect = texte_surface.get_rect()
        texte_rect.center = (10, 10)

        screen.blit(texte_surface, (1920-90, 50))

        if players.players[2].gun:
            screen.blit(self.gunTexture, (1920-90, 55))

    def set_players_ui(self, screen, players: Players):
        """
        Affiche l'interface utilisateur pour tous les joueurs.

        Args:
            screen (pygame.display): La surface pygame sur laquelle afficher l'interface.
            players (Players): La classe contenant les joueurs.
        """
        self.setUI1(screen, players)
        self.setUI2(screen, players)
        self.setUI3(screen, players)
        self.setUI4(screen, players)


if __name__ == "__main__":
    pygame.init()
    t = Textures()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    playerUI = PlayerUI(t)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_pos = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        playerUI.setUI1(screen)
        playerUI.setUI2(screen)
        playerUI.setUI3(screen)
        playerUI.setUI4(screen)
        pygame.display.flip()

    pygame.quit()
