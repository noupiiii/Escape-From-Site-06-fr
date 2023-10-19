import pygame
import sys
from pygame import mixer
from Guards import Guard, Guards

from Players import Players
from Map import Map
from Save import Save
from Textures import Textures
from Menu import Menu
from Player import Player
from Position import Position
from Cards import Cards
from PlayerUI import PlayerUI
from GestionDes import GestionDes
from Gun import Gun, Guns
from Escpe import Escape


class Main:
    def __init__(self) -> None:
        pygame.init()

        self.window_height = 1080
        self.window_width = 1920

        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height), pygame.FULLSCREEN)

        pygame.display.set_caption("Escape From Site 06")

        self.textures = Textures()

    def menu(self, menu: bool):
        menu = menu
        class_menu = Menu(self.screen)

        # Main music:
        mixer.music.load("assets/musics/main_music.mp3")
        mixer.music.play()

        while menu:

            for event in pygame.event.get():
                self.screen.fill((0, 0, 0))
                result = class_menu.display()
                if result is not None:
                    if result.startswith("save") and result.endswith(".txt"):
                        result = class_menu.menu_play.loadSave(
                            f"./saves/{result}")
                        self.menu(False)
                        self.board_game(True, result)

                if class_menu.handle_events(event) == "+ new game":
                    self.menu(False)
                    self.board_game(True)
                    mixer.music.pause()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

    def board_game(self, board_game_v: bool, saveDicd=None):

        cards = Cards(self.textures.textures, self.screen, saveDicd)
        players = Players(self.textures, self.screen, saveDicd)
        playerui = PlayerUI(self.textures)

        current_turn = 0 if saveDicd is None else int(
            saveDicd["player_turn"][0])

        gestion_des = GestionDes()
        map = Map(self.textures)
        guns = Guns(map.map_list, self.textures, self.screen, saveDicd)
        guards = Guards(map.map_list, self.textures, self.screen, saveDicd)

        cards.create_cards(map.map_list)

        tour_count = 1

        escapeMenu = Escape(self.screen)
        clock = pygame.time.Clock()

        while board_game_v:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if escapeMenu.visible == False:
                    # Remplir l'écran de noir (évite les bugs graphiques)
                    self.screen.fill((0, 0, 0))

                    # Afficher la carte
                    map.display(self.screen)

                    # Définit le joueur actuel
                    current_player = players.players[current_turn % 4]

                    # Permet au joueur actuel de se déplacer
                    current_player.input(event, map, map._zones_bloquees)

                    # Lance la première fois le dé.
                    if gestion_des.random_value is None:
                        gestion_des.lancer_de()

                    # Si le joueur à consumer tout ses déplacements, on passe au joueur suivant.
                    if gestion_des.random_value == current_player.move_count or gestion_des.random_value < current_player.move_count:
                        current_player.move_count = 0
                        gestion_des.lancer_de()
                        # Passe au joueur suivant
                        if (current_turn + 1) % 4 == 0:
                            tour_count = tour_count + 1
                            guards.automove(self.screen)

                        current_turn = (current_turn + 1) % 4

                    # Affiche le nombre de coups restants.
                    gestion_des.display(self.screen, current_player)

                    # Affiche le joueur actuel
                    players.display()

                    # Affiche les cartes sur la map et dans l'interface.
                    cards.display()

                    # Affiche le joueur actuel.
                    current_player.display_player_turn(
                        self.screen, self.textures)

                    # Affiches les armes sur la map
                    guns.display()

                    guards.display()

                    playerui.set_players_ui(self.screen, players)

                    # Détecte les cartes récupérées.
                    cards.detecte_recuperer_carte(
                        current_player.position, self.screen, self.textures, map)

                    guns.detecte_gun_recuperer(
                        current_player.position, current_player)

                    guards.detecte_gun_recuperer(current_player)

                    current_player.display(self.screen)

                    escapeMenu.detecte_escape(event)
                else:

                    if escapeMenu.display(event) == False:
                        self.board_game(False)
                        self.menu(True)
                    elif escapeMenu.display(event) == "save":
                        save = Save()
                        save.save([players.players[0].position, players.players[1].position, players.players[2].position, players.players[3].position], current_turn, [
                            players.players[0].gun, players.players[1].gun, players.players[2].gun, players.players[3].gun], guns.guns, guards.guard, [cards.card_1, cards.card_2, cards.card_3, cards.card_4], [cards.card_1.visible_ui, cards.card_2.visible_ui, cards.card_3.visible_ui, cards.card_4.visible_ui])
                        print("save")
                fps = int(clock.get_fps())
                font = pygame.font.Font("assets/fonts/iknowaghost.ttf", 20)
                text = font.render(f"FPS: {fps}", True, (255, 255, 255))
                self.screen.blit(text, (250, 1080 - 50))

            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":

    game = Main()
    game.menu(True)
    game.board_game(False)
