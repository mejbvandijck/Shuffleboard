#An errorneos programm made by ChatGPT
class Shuffleboard:
    def __init__(self):
        self.players_list = {}

    def create_players(self):
        player_number = 1
        while True:
            player_name = input(f"Enter name for player{player_number} (hit Enter to stop): ")
            if not player_name:
                break
            player = Player(player_name)
            self.players_list[player] = player_name
            player_number += 1

    def layout_shuffleboard(self, round_number):
        layout = []
        players_names = list(self.players_list.values())
        layout.append([''] + players_names)

        for i in range(1, round_number + 2):
            if i == 1:
                layout.append(['Round', f'Round{i}'] + ['-'] * len(players_names))
            else:
                layout.append([''] * (len(players_names) + 2))

        return layout

    def print_board(self, round_number):
        layout = self.layout_shuffleboard(round_number)
        for row in layout:
            print(' '.join(map(str, row)))

    def play_round(self, round_number):
        for player, name in self.players_list.items():
            score = input(f"{name}, enter your score for Round{round_number}: ")
            while score and (not score.isdigit() or not 0 < int(score) <= 148):
                print("Invalid score. Please enter a valid score (0 < score <= 148) or hit Enter to quit.")
                score = input(f"{name}, enter your score for Round{round_number}: ")

            if not score:
                quit_option = input(f"Do you want to quit, {name}? (Yes/No, default is Yes): ").lower()
                if quit_option != 'no':
                    del self.players_list[player]
                    continue

            player.add_score(int(score))

    def play_game(self):
        round_number = 1
        while self.players_list and round_number <= 10:
            self.print_board(round_number)
            self.play_round(round_number)
            round_number += 1

        print("Final Results:")
        self.print_board(round_number - 1)
        self.display_results()

    def display_results(self):
        print("Thank you for using this program.")
        input("Press Enter to exit.")


class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_total_score(self):
        return sum(self.scores)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)


if __name__ == "__main__":
    shuffleboard_game = Shuffleboard()
    shuffleboard_game.create_players()
    shuffleboard_game.play_game()
