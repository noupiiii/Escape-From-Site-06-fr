import ast
import pygame
import random as rd
from pygame import mixer

from Entity import Entity
from Map import Map
from Player import Player
from Position import Position
from Textures import Textures


class Guard:
    def __init__(self, position: Position, textures: Textures) -> None:

        self.sound_kill = mixer.Sound("assets/sounds/kill.wav")
        self.sound_jail = mixer.Sound("assets/sounds/door.mp3")

        self.inaccessible_cases = ['X', 'A']

        self.window_center_x = 1920 // 2
        self.window_center_y = 1080 // 2

        self.position: Position = position

        self.texture = textures.textures["guard"]
        self.texture = pygame.transform.scale(self.texture, (24, 24))

        self.visible = True

    def move(self, new_position: Position, map: list) -> None:
        self.position: Position = new_position

    def id_valid_move(self, x, y, map) -> None:
        print("valid")
        if ((x >= 0 and x+1 <= 30) and (y >= 0 and y+1 <= 20)):
            print("test")
            if map[y][x] in self.inaccessible_cases:
                print(map[y][x])
                return False
            else:
                return True

    def auto_move(self, distance: int, map: Map, screen):
        for _ in range(1):
            move = 0
            while move < 5:
                print(move)
                sens = rd.randint(1, 4)
                if sens == 1:
                    x, y = self.position.x, self.position.y + 1
                elif sens == 2:
                    x, y = self.position.x + 1, self.position.y
                elif sens == 3:
                    x, y = self.position.x, self.position.y - 1
                else:
                    x, y = self.position.x - 1, self.position.y

                if self.id_valid_move(x, y, map):
                    self.position.x, self.position.y = x, y
                    move = move + 1

    def display(self, screen: pygame.display):
        if self.visible:
            x_pos = (self.position.x - 15) * 32 + self.window_center_x + 4
            y_pos = (self.position.y - 10) * 32 + self.window_center_y + 4
            screen.blit(self.texture, (x_pos, y_pos))

    def detecte_player(self, current_player: Player, index, guards):
        if self.position.x == current_player.position.x and self.position.y == current_player.position.y:
            if current_player.gun:
                self.visible = False
                guards.guard.pop(index)
                self.sound_kill.play()
                current_player.gun = False
            else:
                current_player.position = Position(0, 0)
                current_player.move_count = 10
                self.sound_jail.play()


class Guards:
    def __init__(self, map: list, textures: Textures, screen: pygame.display, saveDict=None) -> None:

        self.saveDict = saveDict
        self.map = map

        self.inaccessible_cases = ['X', 'A']

        self.screen = screen

        self.textures = textures
        guards_positions = []
        self.guard = []

        if self.saveDict is None:
            for x in range(30):
                for y in range(20):
                    if map[y][x] not in self.inaccessible_cases:
                        if rd.randint(0, 100) > 95:
                            guards_positions.append((x, y))

            for guard in range(len(guards_positions)):
                self.guard.append(Guard(Position(
                    guards_positions[guard][0], guards_positions[guard][1]), self.textures))
            self.map = map
        else:
            num_positions = len(saveDict["guards_positions"])
            for i in range(num_positions):
                guards_position = saveDict.get(
                    "guards_positions", [(0, 0)])[i - 1]
                valeur_tuple = ast.literal_eval(guards_position)

                # Assurez-vous que la valeur est bien un tuple
                if isinstance(valeur_tuple, tuple) and len(valeur_tuple) == 2:
                    x, y = valeur_tuple
                guard = Guard(Position(x, y), self.textures)
                self.guard.append(guard)

    def display(self):
        for i in range(len(self.guard)):
            self.guard[i].display(self.screen)

    def detecte_gun_recuperer(self, current_player: Player):
        for index, i in enumerate(self.guard):
            i.detecte_player(current_player, index, self)

    def automove(self, screen):
        for guards in self.guard:
            guards.auto_move(10, self.map, screen)
