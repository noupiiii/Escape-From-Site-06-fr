import pygame


class Textures:
    def __init__(self) -> None:
        self.textures = {

            # Importation des obj :
            "gun": pygame.image.load("assets/obj/gun.png"),

            # Textures de cartes :
            "card1": pygame.image.load("assets/cartes/carte_1.png"),
            "card2": pygame.image.load("assets/cartes/carte_2.png"),
            "card3": pygame.image.load("assets/cartes/carte_3.png"),
            "card4": pygame.image.load("assets/cartes/carte_4.png"),

            # Textures des entitées :
            "player1": pygame.image.load("assets/entity/player1.png"),
            "player2": pygame.image.load("assets/entity/player2.png"),
            "player3": pygame.image.load("assets/entity/player3.png"),
            "player4": pygame.image.load("assets/entity/player4.png"),

            "player1_selected": pygame.image.load("assets/entity/player1_selected.png"),
            "player2_selected": pygame.image.load("assets/entity/player2_selected.png"),
            "player3_selected": pygame.image.load("assets/entity/player3_selected.png"),
            "player4_selected": pygame.image.load("assets/entity/player4_selected.png"),

            "guard": pygame.image.load("assets/entity/guard.png"),

            # Textures de la carte :
            "I": pygame.image.load("assets/map_textures/sol_simple.png"),
            "B": pygame.image.load("assets/map_textures/sol_noir.png"),
            "C": pygame.image.load("assets/map_textures/sol_bois.png"),
            "A": pygame.image.load("assets/map_textures/depart_classd.png"),
            "F": pygame.image.load("assets/map_textures/fin.png"),
            "S": pygame.image.load("assets/map_textures/scp_confinement.png"),
            "X": pygame.image.load("assets/map_textures/void.png"),
            "U": pygame.image.load("assets/map_textures/door.png"),
            "V": pygame.image.load("assets/map_textures/door_b_n.png"),
            "W": pygame.image.load("assets/map_textures/door_b_w.png"),

            # Importation des UI
            "arrow": pygame.image.load("assets/ui/arrow.png"),
            "light_ui": pygame.image.load("assets/ui/light_ui.png"),
            "light_ui_down": pygame.image.load("assets/ui/light_ui_down.png"),

            "zone1": pygame.image.load("assets/ui/zone1.png"),
            "zone2": pygame.image.load("assets/ui/zone2.png"),
            "zone3": pygame.image.load("assets/ui/zone3.png"),

            "logo": pygame.image.load("assets/ui/logo.png")
        }
