# Importation des bibliothèques nécessaires
from pygame import mixer
import pygame
from Map import Map
from Position import Position
from Textures import Textures

# Définition de la classe Card


class Card:

    def __init__(self, position: Position, texture: pygame.image, id: int) -> None:
        """Constructeur par défaut de card. Il permet de définir les attributs importants d'une carte

        Args:
            position (Position): La position de la carte
            texture (pygame.image): La texture de la carte
            id (int): L'identifiant de la carte
        """

        # Importation du son de pickup_card
        self.card_pickup = mixer.Sound("assets/sounds/pickup.wav")

        # Initialisation des propriétés de la carte
        self.position = position  # Position de la carte sur la carte du jeu
        self.texture = texture  # Texture de la carte
        self.id = id  # Identifiant de la carte

        self.size = 32  # Taille de la carte

        self.window_center_x = 1920 // 2  # Centre de la fenêtre
        self.window_center_y = 1080 // 2

        self.visible_ui = False  # Indicateur de visibilité de l'interface utilisateur
        self.visible_board = True  # Indicateur de visibilité sur la carte du jeu

    def display_on_map(self, screen: pygame.display):
        """Affiche la carte sur la carte du jeu si elle est visible.

        Args:
            screen (pygame.display): La surface d'affichage sur laquelle la carte sera dessinée.
        """

        if self.visible_board:
            # Transforme la taille des cellules (les réduit à 32 pixels)
            self.texture = pygame.transform.scale(
                self.texture, (self.size, self.size))
            # Calcule la position x et y de la cellule.
            x_pos = (self.position.x - 15) * self.size + self.window_center_x
            y_pos = (self.position.y - 10) * self.size + self.window_center_y
            # Affiche la cellule.
            screen.blit(self.texture, (x_pos, y_pos))

    def display_ui(self, screen: pygame.display):
        """Affiche la carte dans l'interface utilisateur (UI) si elle est visible.
        La position de l'affichage dépend de l'identifiant de la carte.

        Args:
            screen (pygame.display): La surface d'affichage de l'interface utilisateur.
        """

        if self.id == 1 and self.visible_ui:
            screen.blit(self.texture, (((1920 // 2) - 25) - 75, 0))
        elif self.id == 2 and self.visible_ui:
            screen.blit(self.texture, (((1920 // 2) - 25) - 25, 0))
        elif self.id == 3 and self.visible_ui:
            screen.blit(self.texture, (((1920 // 2) - 25) + 25, 0))
        elif self.id == 4 and self.visible_ui:
            screen.blit(self.texture, (((1920 // 2) - 25) + 75, 0))

    def detecte_carte_recuprer(self, player_position: Position, screen: pygame.display, textures: Textures, map: Map):
        """Détecte si le joueur a récupéré la carte et gère la visibilité de la carte.
        Si le joueur a récupéré la carte, la carte devient visible dans l'interface utilisateur (UI)
        et invisible sur la carte du jeu.

        Args:
            player_position (Position): La position du joueur.
            screen (pygame.display): La surface d'affichage.
            textures (Textures): Les textures utilisées dans le jeu.
            map (Map): La carte du jeu.
        """

        if player_position.x == self.position.x and player_position.y == self.position.y:
            self.visible_ui = True
            self.visible_board = False
            if self.visible_board:
                self.card_pickup.play()
        self.bloquer_zones_ui(screen, textures, map)

    def bloquer_zones_ui(self, screen: pygame.display, textures: Textures, map: Map):
        """Gère le blocage des zones de l'interface utilisateur en fonction de l'identifiant de la carte.
        Cela peut inclure l'affichage de textures spécifiques sur l'interface utilisateur et la modification
        de zones bloquées sur la carte du jeu.

        Args:
            screen (pygame.display): La surface d'affichage de l'interface utilisateur.
            textures (Textures): Les textures utilisées dans le jeu.
            map (Map): La carte du jeu.
        """

        if self.visible_board and self.id == 1:
            screen.blit(textures.textures["zone1"], (0, 0))
        if self.visible_ui and self.id == 1:
            map._zones_bloquees[3] = 0

        if self.visible_board and self.id == 2:
            screen.blit(textures.textures["zone2"], (0, 0))
        if self.visible_ui and self.id == 2:
            map._zones_bloquees[1] = 0

        if self.visible_board and self.id == 3:
            screen.blit(textures.textures["zone3"], (0, 0))
        if self.visible_ui and self.id == 3:
            map._zones_bloquees[2] = 0
