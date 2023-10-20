import pygame
from Textures import Textures
from Tile import Tile


class Map:

    def __init__(self, textures_list: Textures) -> None:
        """Constructeur de la classe Map. Initialise la carte du jeu.

        Args:
            textures_list (Textures): Liste de textures utilisées pour la carte.
        """
        self.map_width = 30
        self.map_height = 20

        self.window_center_x = 1920 // 2
        self.window_center_y = 1920 // 2

        self.textures = textures_list

        # Charge la carte du fichier texte et crée la liste de tuiles
        self.map_list = self.text_to_list()
        self.map_tile_list = self.map_creator()

        self._zones_bloquees = ['X', (22, 11), (16, 13), (14, 5)]

    def text_to_list(self) -> list[str]:
        """Convertit le texte de la carte en une liste de chaînes de caractères.

        Returns:
            list[str]: Liste de chaînes de caractères représentant la carte.
        """
        map_list = []
        with open('map.txt', 'r') as fichier:
            lignes = fichier.readlines()
        liste_de_listes = []
        for ligne in lignes[:20]:
            ligne_liste = ligne.strip().split()
            liste_de_listes.append(ligne_liste)

        for liste in liste_de_listes:
            map_list.append(liste)
        return map_list

    def map_creator(self):
        """Crée la liste de tuiles pour la carte du jeu.

        Returns:
            list[Tile]: Liste d'objets Tile représentant la carte du jeu.
        """
        map_tile_list = []
        for x in range(self.map_width):
            for y in range(self.map_height):
                correspondance_key = self.map_list[y][x]
                tile_texture = self.textures.textures[correspondance_key]
                tile = Tile(x, y, tile_texture)
                map_tile_list.append(tile)
        return map_tile_list

    def display(self, screen: pygame.display):
        """Affiche la carte du jeu sur l'écran.

        Args:
            screen (pygame.display): Surface d'affichage.
        """
        for tile in self.map_tile_list:
            tile.display(screen)
