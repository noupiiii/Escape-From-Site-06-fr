class Position:
    def __init__(self, x, y):
        if isinstance(x, tuple):
            self.x, self.y = x
        else:
            self.x = x
            self.y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    def copy(self):
        # Constructeur par recopie
        return Position(self._x, self._y)

    def __str__(self):
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
