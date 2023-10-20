import pygame
from Position import Position


class Button:
    """Classe représentant un bouton dans l'interface graphique.

    Attributes:
        screen (pygame.Surface): La surface Pygame sur laquelle est affiché le bouton.
        button_name (str): Le texte du bouton.
        position (Position): La position du bouton.
        callback (callable, optional): La fonction à appeler lorsque le bouton est cliqué.

    Methods:
        display(): Affiche le bouton à l'écran.
        hovered(): Détecte si le bouton est survolé.
        detecte_hovered(event): Détecte si le bouton est survolé.
        detect_clicked(event): Retourne le nom du bouton s'il est cliqué.
    """

    def __init__(self, screen: pygame.Surface, button_name: str, position: Position, callback=None):
        """Constructeur principal de la classe Button. Cette fonction permet de créer un bouton
        en position passée en paramètres.

        Args:
            screen (pygame.Surface): Fenêtre sur laquelle est affiché le bouton.
            button_name (str): Le texte du bouton.
            position (Position): La position du bouton.
            callback (callable, optional): La fonction à appeler lorsque le bouton est cliqué.
        """

        # Initialisation des propriétés du bouton
        self.button_name: str = button_name  # Le texte du bouton
        self.screen: pygame.Surface = screen
        self.position: Position = position  # La position du bouton
        self.visible: bool = False  # Indicateur de visibilité du bouton

        # Chargement de la police pour le texte du bouton
        self.font: str = "assets/fonts/iknowaghost.ttf"  # Texture de la police
        self.font: pygame.font.Font = pygame.font.Font(
            self.font, 50)  # Texte + Taille

        # Couleurs pour le texte du bouton
        self.color: tuple = (255, 255, 255)  # Couleur par défaut
        self.hoveredColor: tuple = (255, 128, 0)

    def display(self):
        """Procédure permettant d'afficher le bouton à l'écran.
        """
        # Affiche le bouton sur l'écran si visible
        if self.visible:
            self.screen.blit(self.font.render(
                self.button_name, True, self.color), (self.position.x, self.position.y))

    def hovered(self):
        """Procédure détectant si le bouton est survolé.
        """
        # Affiche le bouton avec la couleur survolée si visible
        if self.visible:
            self.screen.blit(self.font.render(
                self.button_name, True, self.hoveredColor), (self.position.x, self.position.y))

    def detecte_hovered(self, event):
        """Fonction détectant si le bouton est survolé.

        Args:
            event (pygame.event): Détecte le clic de la souris.

        Returns:
            bool: Le bouton est survolé ou non.
        """
        # Détecte si la souris survole le bouton
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_width: int = 200
        button_height: int = 50

        # Si la souris est sur le bouton.
        if self.position.x < mouse_x < self.position.x + button_width and \
           self.position.y < mouse_y < self.position.y + button_height:
            self.hovered()  # Change la couleur lorsque survolé
            return True
        else:
            self.display()  # Affiche avec la couleur par défaut
            return False

    def detect_clicked(self, event):
        """Fonction retournant le nom du bouton s'il est cliqué.

        Args:
            event (pygame.event): Détecte le clic de la souris.

        Returns:
            str: Nom du bouton.
        """
        # Détecte si le bouton est cliqué
        if self.visible:
            if self.detecte_hovered(event) and event.type == pygame.MOUSEBUTTONDOWN:
                return self.button_name  # Retourne le nom du bouton si cliqué
