from pygame import mixer
import pygame
from Map import Map
from Position import Position
from Textures import Textures

# Définition de la classe Card


class Card:
    def __init__(self, position: Position, texture, id) -> None:

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
        # Affiche la carte sur la carte du jeu si elle est visible
        if self.visible_board:
            self.texture = pygame.transform.scale(
                self.texture, (self.size, self.size))
            x_pos = (self.position.x - 15) * self.size + self.window_center_x
            y_pos = (self.position.y - 10) * self.size + self.window_center_y
            screen.blit(self.texture, (x_pos, y_pos))

    def display_ui(self, screen: pygame.display):
        # Affiche la carte dans l'interface utilisateur (UI) si elle est visible
        if self.id == 1 and self.visible_ui:
            screen.blit(self.texture, (((1920 // 2) - 25) - 75, 0))
        elif self.id == 2 and self.visible_ui:
            screen.blit(self.texture, (((1920 // 2) - 25) - 25, 0))
        elif self.id == 3 and self.visible_ui:
            screen.blit(self.texture, (((1920 // 2) - 25) + 25, 0))
        elif self.id == 4 and self.visible_ui:
            screen.blit(self.texture, (((1920 // 2) - 25) + 75, 0))

    def detecte_carte_recuprer(self, player_position: Position, screen: pygame.display, textures: Textures, map: Map):
        # Détecte si le joueur a récupéré la carte et gère la visibilité
        if player_position.x == self.position.x and player_position.y == self.position.y:
            self.visible_ui = True
            self.visible_board = False
            if self.visible_board:
                self.card_pickup.play()
        self.bloquer_zones_ui(screen, textures, map)

    def bloquer_zones_ui(self, screen: pygame.display, textures: Textures, map: Map):
        # Gère le blocage des zones de l'interface utilisateur en fonction de l'identifiant de la carte
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
