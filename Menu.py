import pygame
import sys
from Button import Button
from Position import Position
from MenuPlay import MenuPlay
from MenuBox import MenuBox


class Menu:
    """Ce module gère le menu principal du jeu.

    Il permet aux joueurs de démarrer une nouvelle partie, d'accéder aux règles, aux crédits
    et de quitter le jeu.

    Attributes:
        screen: La surface d'affichage du jeu.
        buttons (list[Button]): Une liste de boutons du menu.

    Methods:
        show_menu_play(): Affiche le menu de jeu et masque le titre.
        display(): Affiche les éléments du menu sur l'écran.
        handle_events(event): Gère les événements, y compris les clics sur les boutons du menu.
        toggle_menu_play(): Gère l'affichage du menu de jeu.
    """

    def __init__(self, screen) -> None:
        """Initialise le menu.

        Args:
            screen: La surface de l'écran du jeu.
        """
        self.screen = screen
        self.buttons = []

        # Crée un titre de jeu
        self.gameT = GameTitle("Escape From Site 06_fr", screen)

        # Crée un menu de jeu
        self.menu_play = MenuPlay(self.screen)
        self.menu_play.newGameButton.visible = False
        self.buttons.append(self.menu_play.newGameButton)

        # Crée un bouton "Play" qui permet d'afficher le MenuPlay
        button1_position = Position(x=100, y=300)
        # Lorsque ce bouton est cliqué, il appelle la fonction show_menu_play
        button1 = Button(self.screen, "Play",
                         button1_position, self.show_menu_play)
        button1.visible = True
        self.buttons.append(button1)

        # Crée un bouton "Rules"
        button2_position = Position(x=100, y=400)
        button2 = Button(self.screen, "Rules", button2_position)
        button2.visible = True
        self.buttons.append(button2)

        # Crée un bouton "Credits"
        button3_position = Position(x=100, y=500)
        button3 = Button(self.screen, "Credits", button3_position)
        button3.visible = True
        self.buttons.append(button3)

        # Crée un bouton "Quit" qui permet de quitter le jeu
        button4_position = Position(x=100, y=600)
        # Lorsque ce bouton est cliqué, il appelle sys.exit pour quitter le jeu
        button4 = Button(self.screen, "Quit", button4_position, sys.exit)
        button4.visible = True
        self.buttons.append(button4)

    def show_menu_play(self):
        """Affiche le menu de jeu et masque le titre."""
        self.menu_box.visible = False
        self.gameT.visible = False

    def display(self):
        """Affiche les éléments du menu sur l'écran.

        Returns:
            bool: Un indicateur du menu de sauvegarde.
        """
        for button in self.buttons:
            button.display()
        self.gameT.display()
        self.menu_play.frame.display()
        return self.menu_play.allSavesDisplay()

    def handle_events(self, event):
        """Gère les événements, notamment les clics sur les boutons du menu.

        Args:
            event: L'événement pygame en cours de traitement.
        """
        for button in self.buttons:
            clicked_button_name = button.detect_clicked(event)
            if clicked_button_name == "Play":
                self.toggle_menu_play()
            if clicked_button_name == "+ new game":
                return clicked_button_name
            if clicked_button_name == "Quit":
                pygame.quit()

    def toggle_menu_play(self):
        """Gère l'affichage du menu de jeu.

        Ce bouton permet d'afficher ou de masquer le menu de jeu et la création d'une nouvelle partie.
        """
        self.menu_play.allSavesToString(self.menu_play.loadSaves())
        if self.menu_play.newGameButton.visible == True:
            self.menu_play.newGameButton.visible = False
            self.menu_play.frame.visible = False
        else:
            self.menu_play.newGameButton.visible = True
            self.menu_play.frame.visible = True


class GameTitle:
    def __init__(self, titleName, screen) -> None:
        """Initialise le titre du jeu.

        Args:
            titleName (str): Le nom du jeu.
            screen: La surface de l'écran du jeu.
        """
        self.screen = screen
        self.titleName = titleName

        self.font = "assets/fonts/iknowaghost.ttf"
        self.font = pygame.font.Font(self.font, 100)

        self.visible = True
        self.color = (255, 255, 255)

        self.position = Position(100, 100)

    def display(self):
        """Affiche le titre du jeu à l'écran."""
        self.screen.blit(self.font.render(
            self.titleName, True, self.color), (self.position.x, self.position.y))
