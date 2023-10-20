import random as rd
from Position import Position
from Map import Map


class Entity:
    def __init__(self, position: Position, name: str) -> None:
        """Constructeur de la classe Entity. Initialise la position et le nom de l'entité.

        Args:
            position (Position): La position de l'entité.
            name (str): Le nom de l'entité.
        """
        self.position: Position = position
        self.name: str = name
        self.inaccessible_cases = ['X', 'A']

    def move(self, new_position: Position) -> None:
        """Modifie la position de l'entité en déplaçant l'entité vers une nouvelle position spécifiée.

        Args:
            new_position (Position): La nouvelle position vers laquelle l'entité doit être déplacée.
        """
        self.position: Position = new_position

    def auto_move(self, distance: int) -> None:
        """Cette fonction est actuellement commentée, mais elle semble être destinée à gérer le déplacement automatique de l'entité sur une certaine distance. Cependant, le code pour ce déplacement automatique est actuellement en commentaire et doit être décommenté et implémenté pour fonctionner correctement.

        Args:
            distance (int): La distance sur laquelle l'entité doit se déplacer automatiquement.
        """
        # for deplacement in range(rd.randint(0, distance)):
        pass
