from pygame import mixer
import pygame
from Map import Map
from Position import Position
from Textures import Textures


class Player:
    def __init__(self, position: Position, id: int, texture: Textures) -> None:
        self.position = position
        self.id = id
        self.texture: Textures = texture
        self.texture = pygame.transform.scale(self.texture, (24, 24))

        self.sound_move = mixer.Sound("assets/sounds/step.wav")
        self.sound_error = mixer.Sound("assets/sounds/error.wav")

        self.endurence = 0

        self.window_center_x = 1920 // 2
        self.window_center_y = 1080 // 2

        self.move_count = 0

        self.font = "assets/fonts/iknowaghost.ttf"

        self.gun = False
        if self.gun:
            print("joueur"+self.id+" a une arme")

    def display(self, screen: pygame.display):
        x_pos = (int(self.position.x) - 15) * 32 + self.window_center_x + 4
        y_pos = (int(self.position.y) - 10) * 32 + self.window_center_y + 4
        screen.blit(self.texture, (x_pos, y_pos))

    def display_player_turn(self, screen: pygame.display, textures: Textures):
        players_names = ["Abigail Briarton", "Marlton Johnson",
                         "Samantah Maxis",  "Edward Richtofen"]
        toBlit = "Player turn :  "+str(players_names[self.id-1])
        font = pygame.font.Font(self.font, 50)
        texte_surface = font.render(toBlit, True, (255, 127, 0))

        texte_rect = texte_surface.get_rect()
        texte_rect.center = (10, 10)

        screen.blit(texte_surface, ((1920//2) - texte_rect.width//2, 100))

        arrow_texture = textures.textures["arrow"]
        arrow_texture = pygame.transform.scale(arrow_texture, (30, 25))
        if self.id == 1:
            arrow_texture = pygame.transform.rotate(arrow_texture, 180)
            screen.blit(arrow_texture, (200, 50))
        if self.id == 2:
            arrow_texture = pygame.transform.rotate(arrow_texture, 180)
            screen.blit(arrow_texture, (200, 1080-75))
        if self.id == 3:
            screen.blit(arrow_texture, (1920 - 250, 50))
        if self.id == 4:
            screen.blit(arrow_texture, (1920 - 250, 1080 - 75))

    def move_player(self, x: int, y: int):
        self.position = Position(x, y)

    def input(self, event: pygame.event, map: Map, zones_bloquees):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.valid_move(map.map_list, self.position.x - 1, self.position.y, zones_bloquees):
                    self.move_player(self.position.x - 1, self.position.y)
                    self.move_count += 1
            elif event.key == pygame.K_RIGHT:
                if self.valid_move(map.map_list, self.position.x + 1, self.position.y, zones_bloquees):
                    self.move_player(self.position.x + 1, self.position.y)
                    self.move_count += 1
            elif event.key == pygame.K_UP:
                if self.valid_move(map.map_list, self.position.x, self.position.y - 1, zones_bloquees):
                    self.move_player(self.position.x, self.position.y - 1)
                    self.move_count += 1
            elif event.key == pygame.K_DOWN:
                if self.valid_move(map.map_list, self.position.x, self.position.y + 1, zones_bloquees):
                    self.move_player(self.position.x, self.position.y + 1)
                    self.move_count += 1

    def valid_move(self, map: list, x: int, y: int, zones_bloquees):
        if ((x >= 0 and x+1 <= 30) and (y >= 0 and y+1 <= 20)):
            if map[y][x] in zones_bloquees or (x, y) in zones_bloquees:
                self.sound_error.play()
                return False
            else:
                self.sound_move.play()
                return True
