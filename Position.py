class Position:
    def __init__(self, x, y):
        """
        Initialise une instance de Position avec les coordonnées x et y.

        Args:
            x (int): La coordonnée x.
            y (int): La coordonnée y.
        """
        if isinstance(x, tuple):
            self.x, self.y = x
        else:
            self.x = x
            self.y = y

    @property
    def x(self):
        """
        La coordonnée x.

        Returns:
            int: La coordonnée x.
        """
        return self._x

    @property
    def y(self):
        """
        La coordonnée y.

        Returns:
            int: La coordonnée y.
        """
        return self._y

    @x.setter
    def x(self, value):
        """
        Définit la coordonnée x.

        Args:
            value (int): La nouvelle valeur de la coordonnée x.
        """
        self._x = value

    @y.setter
    def y(self, value):
        """
        Définit la coordonnée y.

        Args:
            value (int): La nouvelle valeur de la coordonnée y.
        """
        self._y = value

    def copy(self):
        """
        Crée une nouvelle instance de Position en copiant les coordonnées actuelles.

        Returns:
            Position: Une nouvelle instance de Position avec les mêmes coordonnées.
        """
        return Position(self._x, self._y)

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de la Position.

        Returns:
            str: Une chaîne de caractères représentant la Position au format "(x, y)".
        """
        return f"({self._x}, {self._y})"


if __name__ == "__main__":
    p1 = Position(3, 4)
    print(p1)  # Affiche "(3, 4)"

    # Utilisation des getters et setters
    p1.x = 5
    p1.y = 6
    print(p1.x)  # Affiche 5
    print(p1.y)  # Affiche 6

    # Constructeur par recopie
    p2 = p1.copy()
    print(p2)  # Affiche "(5, 6)"
