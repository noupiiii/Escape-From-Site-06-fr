import ast
from Card import Card
from Position import Position
import random as rd
import pygame


class Cards:
    def __init__(self, textures, screen: pygame.display, saveDict=None) -> None:
        self.cards_list = []

        self.textures = textures
        self.screen = screen

        self.saveDict: dict = saveDict

    def create_cards(self, map: list):
        if self.saveDict is None:
            possible_card_1 = []
            possible_card_2 = []
            possible_card_3 = []
            possible_card_4 = []

            for x in range(29):
                for y in range(19):
                    if map[y][x] == "I":
                        possible_card_1.append((x, y))
                    if map[y][x] == "B" and y < 12:
                        possible_card_2.append((x, y))
                    if map[y][x] == "C":
                        possible_card_3.append((x, y))
                    if map[y][x] == "B" and y > 11:
                        possible_card_4.append((x, y))

            indice = rd.randint(0, len(possible_card_1))
            position_card_1 = Position(
                possible_card_1[indice][0], possible_card_1[indice][1])
            self.card_1 = Card(position_card_1, self.textures["card1"], 1)

            indice = rd.randint(0, len(possible_card_2))
            position_card_2 = Position(
                possible_card_2[indice][0], possible_card_2[indice][1])
            self.card_2 = Card(position_card_2, self.textures["card2"], 2)

            indice = rd.randint(0, len(possible_card_3))
            position_card_3 = Position(
                possible_card_3[indice][0], possible_card_3[indice][1])
            self.card_3 = Card(position_card_3, self.textures["card3"], 3)

            indice = rd.randint(0, len(possible_card_4))
            position_card_4 = Position(
                possible_card_4[indice][0], possible_card_4[indice][1])
            self.card_4 = Card(position_card_4, self.textures["card4"], 4)

            self.cards_list = [self.card_1,
                               self.card_2, self.card_3, self.card_4]

        else:
            for i in range(4):
                cards_position = self.saveDict.get(
                    "cards_positions", [(0, 0)])[i - 1]
                valeur_tuple = ast.literal_eval(cards_position)

                # Assurez-vous que la valeur est bien un tuple
                if isinstance(valeur_tuple, tuple) and len(valeur_tuple) == 2:
                    x, y = valeur_tuple
                card = Card(Position(x, y), self.textures[f'card{i+1}'], i)
                self.cards_list.append(card)

            for i in range(4):
                valeur_gun = eval(self.saveDict["cards_pickup"][i])
                print(valeur_gun)
                self.cards_list[i].visible_ui = valeur_gun

            #     self.cards_list[i].visible_ui = valeur_gun
            #     print("test")

    def display(self):

        for cards in self.cards_list:
            cards.display_on_map(self.screen)
            cards.display_ui(self.screen)

    def detecte_recuperer_carte(self, player_position: Position, screen: pygame.display, texture, map):

        for cards in self.cards_list:
            cards.detecte_carte_recuprer(player_position, screen, texture, map)
