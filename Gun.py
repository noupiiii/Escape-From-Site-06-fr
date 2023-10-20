import ast
import pygame
import random as rd
from Player import Player
from PlayerUI import PlayerUI
from Position import Position
from Textures import Textures
from Map import Map
from pygame import mixer


class Gun:
    def __init__(self, position: Position, texture: Textures, screen: pygame.display) -> None:
        """Constructeur de la classe Gun. Initialise une arme avec sa position, sa texture et l'écran de jeu.

        Args:
            position (Position): Position de l'arme sur la carte.
            texture (Textures): Textures utilisées pour l'arme.
            screen (pygame.display): Surface d'affichage.
        """
        self.position: Position = position
        self.texture = texture.textures["gun"]

        self.sound_gun_pickup = mixer.Sound("assets/sounds/gun.aiff")

        self.window_center_x = 1920 // 2
        self.window_center_y = 1080 // 2

        self.visible = True

        self.screen = screen
        self.size = 32

        self.recuperer = False

    def display(self):
        """Affiche l'arme sur l'écran."""
        if self.visible == True:
            self.texture = pygame.transform.scale(
                self.texture, (self.size, self.size))

            x_pos = (self.position.x - 15) * self.size + self.window_center_x
            y_pos = (self.position.y - 10) * self.size + self.window_center_y
            self.screen.blit(self.texture, (x_pos, y_pos))

    def detecte_gun_recuprer(self, player_position: Position, current_player: Player, guns, index):
        """Détecte si le joueur a récupéré une arme en interagissant avec elle.

        Args:
            player_position (Position): Position actuelle du joueur.
            current_player (Player): Joueur actuel.
            guns (Guns): Classe de gestion des armes.
            index (int): Index de l'arme.
        """
        if self.recuperer == False:
            if player_position.x == self.position.x and player_position.y == self.position.y:
                self.visible = False
                current_player.gun = True
                self.sound_gun_pickup.play()
                # Retirez l'arme de la liste
                guns.guns.pop(index)


class Guns:
    def __init__(self, map: list, textures: Textures, screen: pygame.display, saveDict=None) -> None:
        """Constructeur de la classe Guns. Initialise la gestion des armes.

        Args:
            map (list): Carte du jeu.
            textures (Textures): Textures utilisées pour les armes.
            screen (pygame.display): Surface d'affichage.
            saveDict (dict, optional): Dictionnaire de sauvegarde. Defaults to None.
        """
        self.saveDict = saveDict

        self.screen = screen

        self.textures = textures
        possible_position = ["I", "B", "C"]
        guns_positions = []
        self.guns = []
        if self.saveDict is None:
            for x in range(30):
                for y in range(20):
                    if map[y][x] in possible_position:
                        if rd.randint(0, 100) > 95:
                            guns_positions.append((x, y))

            for gun in range(len(guns_positions)):
                self.guns.append(
                    Gun(Position(guns_positions[gun][0], guns_positions[gun][1]), self.textures, self.screen))
        else:
            num_positions = len(saveDict["guns_positions"])
            for i in range(num_positions):
                gun_position = saveDict.get(
                    "guns_positions", [(0, 0)])[i - 1]
                valeur_tuple = ast.literal_eval(gun_position)

                # Assurez-vous que la valeur est bien un tuple
                if isinstance(valeur_tuple, tuple) and len(valeur_tuple) == 2:
                    x, y = valeur_tuple
                gun = Gun(Position(x, y),
                          self.textures, self.screen)
                self.guns.append(gun)

    def display(self):
        """Affiche les armes sur l'écran."""
        for gun in range(len(self.guns)):
            self.guns[gun].display()

    def detecte_gun_recuperer(self, player_position: Position, current_player: Player):
        """Détecte si le joueur a récupéré une arme en interagissant avec elle.

        Args:
            player_position (Position): Position actuelle du joueur.
            current_player (Player): Joueur actuel.
        """
        for index, gun in enumerate(self.guns):
            gun.detecte_gun_recuprer(
                player_position, current_player, self, index)
