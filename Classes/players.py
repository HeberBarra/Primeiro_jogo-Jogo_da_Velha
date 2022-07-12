class Player:

    def __init__(self, player_name):
        self.player_name = player_name
        self.plays = []
        self.victories = 0
        self.defeats = 0
        self.draws = 0

    def add_victory(self):
        self.victories += 1

    def add_defeat(self):
        self.defeats += 1

    def add_draw(self):
        self.draws += 1

    def add_play(self, position):
        self.plays.append(position)

    def reset_plays(self):
        self.plays = []

    def detect_victory(self):

        # horizontal lines

        if 0 in self.plays and 1 in self.plays and 2 in self.plays:
            # top horizontal line

            self.add_victory()
            return True

        elif 3 in self.plays and 4 in self.plays and 5 in self.plays:
            # mid horizontal line

            self.add_victory()
            return True

        elif 6 in self.plays and 7 in self.plays and 8 in self.plays:
            # bottom horizontal line

            self.add_victory()
            return True

        # vertical lines

        elif 0 in self.plays and 3 in self.plays and 6 in self.plays:
            # left vertical line

            self.add_victory()
            return True

        elif 1 in self.plays and 4 in self.plays and 7 in self.plays:
            # mid vertical line

            self.add_victory()
            return True

        elif 2 in self.plays and 5 in self.plays and 8 in self.plays:
            # right vertical line

            self.add_victory()
            return True

        # diagonals lines

        elif 0 in self.plays and 4 in self.plays and 8 in self.plays:
            # first diagonal line

            self.add_victory()
            return True

        elif 2 in self.plays and 4 in self.plays and 6 in self.plays:
            # second diagonal line

            self.add_victory()
            return True

        else:
            return False
