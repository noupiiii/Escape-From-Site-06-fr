import pygame

from Textures import Textures
from Tile import Tile


class Map:

    def __init__(self, textures_list: Textures) -> None:

        self.map_width = 30
        self.map_height = 20

        self.window_center_x = 1920 // 2
        self.window_center_y = 1920 // 2

        self.textures = textures_list

        self.map_list = self.text_to_list()
        self.map_tile_list = self.map_creator()

        self._zones_bloquees = ['X', (22, 11), (16, 13), (14, 5)]

    def text_to_list(self) -> list[str]:
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
        map_tile_list = []
        for x in range(self.map_width):
            for y in range(self.map_height):
                correspondance_key = self.map_list[y][x]
                tile_texture = self.textures.textures[correspondance_key]
                tile = Tile(x, y, tile_texture)
                map_tile_list.append(tile)
        return map_tile_list

    def display(self, screen: pygame.display):
        for tile in self.map_tile_list:
            tile.display(screen)
