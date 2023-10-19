import pygame
import sys
from Button import Button
from Position import Position
from MenuPlay import MenuPlay
from MenuBox import MenuBox


class Menu:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.buttons = []

        self.gameT = GameTitle("Escape From Site 06_fr", screen)

        self.menu_play = MenuPlay(self.screen)
        self.menu_play.newGameButton.visible = False
        self.buttons.append(self.menu_play.newGameButton)

        # Create "Play" Button
        button1_position = Position(x=100, y=300)
        # Pass the function to show MenuPlay
        button1 = Button(self.screen, "Play",
                         button1_position, self.show_menu_play)
        button1.visible = True
        self.buttons.append(button1)

        # Create "Rules" Button
        button2_position = Position(x=100, y=400)
        button2 = Button(self.screen, "Rules", button2_position)
        button2.visible = True
        self.buttons.append(button2)

        # Create "Credits" Button
        button3_position = Position(x=100, y=500)
        button3 = Button(self.screen, "Credits", button3_position)
        button3.visible = True
        self.buttons.append(button3)

        # Create "Quit" Button
        button4_position = Position(x=100, y=600)
        # You can pass sys.exit to quit the game
        button4 = Button(self.screen, "Quit", button4_position, sys.exit)
        button4.visible = True
        self.buttons.append(button4)

    def show_menu_play(self):
        self.menu_box.visible = False
        self.gameT.visible = False

    def display(self):
        for button in self.buttons:
            button.display()
        self.gameT.display()
        self.menu_play.frame.display()
        return self.menu_play.allSavesDisplay()

    def handle_events(self, event):
        for button in self.buttons:
            clicked_button_name = button.detect_clicked(event)
            if clicked_button_name == "Play":
                self.toggle_menu_play()
            if clicked_button_name == "+ new game":
                return clicked_button_name
            if clicked_button_name == "Quit":
                pygame.quit()

    def toggle_menu_play(self):

        self.menu_play.allSavesToString(self.menu_play.loadSaves())
        if self.menu_play.newGameButton.visible == True:
            self.menu_play.newGameButton.visible = False
            self.menu_play.frame.visible = False
        else:
            self.menu_play.newGameButton.visible = True
            self.menu_play.frame.visible = True


class GameTitle:
    def __init__(self, titleName, screen) -> None:
        self.screen = screen
        self.titleName = titleName

        self.font = "assets/fonts/iknowaghost.ttf"
        self.font = pygame.font.Font(self.font, 100)

        self.visible = True
        self.color = (255, 255, 255)

        self.position = Position(100, 100)

    def display(self):
        self.screen.blit(self.font.render(
            self.titleName, True, self.color), (self.position.x, self.position.y))
