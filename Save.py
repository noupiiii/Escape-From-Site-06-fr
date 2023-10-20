import datetime
import pathlib

from Position import Position


class Save:
    def __init__(self):
        """
        Initialise un objet de sauvegarde en enregistrant la date actuelle.
        """
        current_datetime = datetime.datetime.now()
        self.date_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    def save(self, players_positions, player_turn, player_gun, guns_position, guards_position, cards_position, cards_pickup):
        """
        Enregistre les données de jeu dans un fichier texte.

        Args:
            players_positions (list[Position]): Les positions des joueurs.
            player_turn (int): Le tour du joueur.
            player_gun (list[bool]): Une liste de booléens indiquant si chaque joueur a une arme.
            guns_position (list[Position]): Les positions des armes.
            guards_position (list[Position]): Les positions des gardes.
            cards_position (list[Position]): Les positions des cartes.
            cards_pickup (list[int]): Les cartes ramassées par les joueurs.
        """
        # Ouvrir un fichier texte en écriture.
        with open(f"./saves/save{self.countFiles()}.txt", "w") as f:

            f.write("date:\n")
            f.write(self.date_string + "\n")

            # Écrire les positions des joueurs.
            f.write("players_positions:\n")
            for position in players_positions:
                f.write(f"({position.x}, {position.y})\n")

            # Écrire le tour du joueur.
            f.write("player_turn:\n" + str(player_turn) + "\n")

            # Écrire la liste des armes des joueurs.
            f.write("player_gun:\n")
            for has_gun in player_gun:
                f.write(str(has_gun) + "\n")

            f.write("guns_positions:\n")
            for position in guns_position:
                f.write(f"({position.position.x},{position.position.y})\n")

            f.write("guards_positions:\n")
            for position in guards_position:
                f.write(f"({position.position.x},{position.position.y})\n")

            f.write("cards_positions:\n")
            for position in cards_position:
                f.write(f"({position.position.x},{position.position.y})\n")

            f.write("cards_pickup:\n")
            for cards in cards_pickup:
                f.write(f"{cards}\n")

        # Fermer le fichier texte.
        f.close()

    def countFiles(self):
        """
        Compte les fichiers de sauvegarde existants dans le répertoire de sauvegarde.

        Returns:
            int: Le nombre de fichiers de sauvegarde existants.
        """
        initial_count = 0
        for path in pathlib.Path("./saves").iterdir():
            if path.is_file():
                initial_count += 1

        return (initial_count)
