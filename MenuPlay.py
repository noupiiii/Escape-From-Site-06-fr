import os
import pygame
from Button import Button
from Position import Position
from MenuBox import MenuBox


class MenuPlay:
    """Classe gérant le menu de chargement de sauvegarde et les nouvelles parties."""

    def __init__(self, screen):
        """Initialise le menu de chargement de sauvegarde.

        Args:
            screen (pygame.Surface): La surface de l'écran du jeu.
        """
        self.screen = screen

        # Initialisation de la police et de la boîte du menu
        self.font = "assets/fonts/iknowaghost.ttf"
        self.font = pygame.font.Font(self.font, 50)
        self.frame = MenuBox(self.screen)

        # Création du bouton "+ new game" et initialisation
        self.newGameButton = Button(
            self.screen, "+ new game", Position(1360, 220))

    def loadSaves(self):
        """Charge les fichiers de sauvegarde depuis le répertoire 'saves'.

        Returns:
            list: Une liste contenant les noms de fichiers et leur contenu.
        """
        self.allSaves = []
        for nom_fichier in os.listdir("./saves"):
            chemin_fichier = os.path.join("./saves", nom_fichier)
            if os.path.isfile(chemin_fichier):
                with open(chemin_fichier, "r") as fichier:
                    contenu = fichier.read()
                    self.allSaves.append((nom_fichier, contenu))
        return self.allSaves

    def allSavesToString(self, allSaves):
        """Convertit les sauvegardes en chaînes de texte."""
        pass

    def saveDisplay(self, position: Position):
        """Affiche un cadre pour une sauvegarde.

        Args:
            position (Position): La position du cadre.
        """
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (position.x, position.y, 250, 150), 1)

    def allSavesDisplay(self):
        """Affiche toutes les sauvegardes sur l'écran.

        Returns:
            str: Le nom du fichier de sauvegarde sélectionné (ou chaîne vide).
        """
        if self.newGameButton.visible:
            fontF = "assets/fonts/iknowaghost.ttf"
            arrow_play = pygame.image.load("assets/ui/arrow.png")
            arrow_play = pygame.transform.scale(arrow_play, (20, 20))

            arrow_play_orange = pygame.image.load("assets/ui/arrow_orange.png")
            arrow_play_orange = pygame.transform.scale(
                arrow_play_orange, (20, 20))

            x, y = 520, 320  # Position initiale
            spacing = 20  # Espace entre les rectangles

            for index, (nom_fichier, contenu) in enumerate(self.allSaves):
                font = pygame.font.Font(fontF, 40)
                self.saveDisplay(Position(x, y))

                # Affiche le nom du fichier dans le cadre
                text_surface = font.render(
                    nom_fichier[:-4], True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.center = (x + 125, y + 75)
                self.screen.blit(text_surface, (x+20, y+10))

                lignes = contenu.split('\n')
                date_sauvegarde = lignes[1] if len(
                    lignes) >= 2 else "Date inconnue"

                font = pygame.font.Font(fontF, 20)
                text_surface = font.render(
                    date_sauvegarde[:-9], True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.bottomright = (x + 230, y + 140)
                self.screen.blit(text_surface, text_rect)

                arrow_rect = pygame.Rect(x+200, y+20, 20, 20)
                # Détecte si la souris est positionnée sur la flèche
                if arrow_rect.collidepoint(pygame.mouse.get_pos()):
                    # Souris sur la flèche
                    # Clic gauche de la souris
                    if pygame.mouse.get_pressed()[0]:
                        # Clic détecté, faites ce que vous voulez ici
                        return nom_fichier

                    self.screen.blit(arrow_play_orange, arrow_rect.topleft)
                else:
                    # Sinon, utilisez la flèche normale
                    self.screen.blit(arrow_play, arrow_rect.topleft)

                # Passez à la colonne suivante après trois rectangles
                if (index + 1) % 4 == 0:
                    x += 250 + spacing  # Largeur du rectangle + espace
                    y = 320  # Revenez à la position initiale en y
                else:
                    y += 150 + spacing

    def loadSave(self, fileName):
        """Charge une sauvegarde à partir d'un fichier.

        Args:
            fileName (str): Le nom du fichier de sauvegarde à charger.

        Returns:
            dict: Les données de la sauvegarde chargée sous forme de dictionnaire.
        """
        # Initialiser un dictionnaire vide pour stocker les données
        data = {}

        # Ouvrir le fichier texte et le lire
        with open(fileName, "r") as fichier:
            lignes = fichier.readlines()

        # Initialiser des variables pour stocker les sections actuelles
        section_actuelle = ""
        section_data = []

        # Parcourir chaque ligne du fichier
        for ligne in lignes:
            # Supprimer les caractères de saut de ligne en fin de ligne
            ligne = ligne.strip()

            # Vérifier si la ligne est une nouvelle section
            if ligne.endswith(":"):
                # Si oui, enregistrer la section précédente (si elle existe)
                if section_actuelle and section_data:
                    data[section_actuelle] = section_data
                # Définir la nouvelle section actuelle
                section_actuelle = ligne[:-1]
                section_data = []
            else:
                # Sinon, ajouter la ligne à la section actuelle
                section_data.append(ligne)

        # Enregistrer la dernière section (si elle existe)
        if section_actuelle and section_data:
            data[section_actuelle] = section_data

        # Maintenant, vous avez un dictionnaire où les clés sont les noms de section et les valeurs sont les données correspondantes
        return data
