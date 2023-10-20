import ast
import pygame
from Position import Position
from Player import Player
from Textures import Textures


class Players:
    def __init__(self, textures: Textures, screen: pygame.display, saveDict=None) -> None:
        """
        Classe représentant un ensemble de joueurs.

        Args:
            textures (Textures): Les textures utilisées pour les joueurs.
            screen (pygame.display): La surface pygame sur laquelle afficher les joueurs.
            saveDict (dict, optional): Un dictionnaire contenant des données de sauvegarde. Par défaut, None.
        """
        self.saveDict = saveDict
        self.screen = screen
        self.textures = textures
        self.players = []

        if saveDict is None:
            allPlayersPos = Position(0, 0)
            for i in range(1, 5):
                player = Player(allPlayersPos, i,
                                textures.textures[f"player{i}"])
                self.players.append(player)
        else:
            for i in range(1, 5):
                player_pos = saveDict.get("players_positions", [(0, 0)])[i - 1]
                valeur_tuple = ast.literal_eval(player_pos)

                # Assurez-vous que la valeur est bien un tuple
                if isinstance(valeur_tuple, tuple) and len(valeur_tuple) == 2:
                    x, y = valeur_tuple
                player = Player(Position(x, y), i,
                                textures.textures[f"player{i}"])
                self.players.append(player)

            for i in range(4):
                valeur_gun = eval(saveDict["player_gun"][i])
                self.players[i].gun = valeur_gun

    def display(self):
        """Affiche tous les joueurs sur l'écran."""
        for player in self.players:
            player.display(self.screen)

    def set_texture_players(self):
        """Définit les textures des joueurs en fonction de leurs numéros."""
        for i, player in enumerate(self.players):
            player.texture = self.textures.textures[f"player{i + 1}"]
