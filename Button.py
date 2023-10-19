import pygame
from Position import Position

# Définition de la classe Button


class Button:
    def __init__(self, screen, button_name, position: Position, callback=None) -> None:
        # Initialisation des propriétés du bouton
        self.button_name = button_name  # Le texte du bouton
        self.screen = screen  # La surface Pygame sur laquelle le bouton sera affiché
        self.position = position  # La position du bouton
        self.visible = False  # Indicateur de visibilité du bouton

        # Chargement de la police pour le texte du bouton
        self.font = "assets/fonts/iknowaghost.ttf"
        self.font = pygame.font.Font(self.font, 50)

        # Couleurs pour le texte du bouton
        self.color = (255, 255, 255)  # Couleur par défaut
        self.hoveredColor = (255, 128, 0)  # Couleur lorsque la souris survole

    def display(self):
        # Affiche le bouton sur l'écran si visible
        if self.visible:
            self.screen.blit(self.font.render(
                self.button_name, True, self.color), (self.position.x, self.position.y))

    def hovered(self):
        # Affiche le bouton avec la couleur survolée si visible
        if self.visible:
            self.screen.blit(self.font.render(
                self.button_name, True, self.hoveredColor), (self.position.x, self.position.y))

    def detecte_hovered(self, event):
        # Détecte si la souris survole le bouton
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_width = 200
        button_height = 50

        if self.position.x < mouse_x < self.position.x + button_width and \
           self.position.y < mouse_y < self.position.y + button_height:
            self.hovered()  # Change la couleur lorsque survolé
            return True
        else:
            self.display()  # Affiche avec la couleur par défaut
            return False

    def detect_clicked(self, event):
        # Détecte si le bouton est cliqué
        if self.visible:
            if self.detecte_hovered(event) and event.type == pygame.MOUSEBUTTONDOWN:
                return self.button_name  # Retourne le nom du bouton si cliqué
