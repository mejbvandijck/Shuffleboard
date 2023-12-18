class Shuffleboard:
    def __init__(self):
        self.playerslist = {}

    def loop_function(self):
        player_number = 1
        while True:
            name = input(f"Enter name for player{player_number} (or hit Enter to stop): ")
            if not name:
                break

            player = Player(name)
            self.playerslist[player] = name
            player_number += 1

    def layout_shuffleboard(self, round_num):
        layout = []
        players_scores = [player.get_score(round_num) for player in self.playerslist.keys()]
        
        # Add players' names in the first row
        layout.append([''] + [self.playerslist[player] for player in self.playerslist.keys()])

        # Add round label and scores
        layout.append([f'Round{round_num + 1}'] + players_scores)

        return layout

    def play_game(self):
        num_rounds = 2  # Minimum rounds to draw
        for round_num in range(num_rounds):
            layout = self.layout_shuffleboard(round_num)
            self.print_layout(layout)

            for player in self.playerslist.keys():
                score = self.get_valid_score(player)
                player.add_score(round_num, score)

        self.print_final_scores()

    def get_valid_score(self, player):
        while True:
            try:
                score = input(f"{self.playerslist[player]}, enter your score (0 < score <= 148 or hit Enter to quit): ")
                if not score:
                    quit_option = input("Do you want to quit the game? (Yes/No, default is Yes): ")
                    if quit_option.lower() != 'no':
                        quit()
                else:
                    score = int(score)
                    if 0 < score <= 148:
                        return score
                    else:
                        print("Invalid score. Please enter a valid score.")
            except ValueError:
                print("Invalid input. Please enter a valid score.")

    def print_layout(self, layout):
        for row in layout:
            print('\t'.join(map(str, row)))

    def print_final_scores(self):
        print("\nFinal Scores:")
        for player, name in self.playerslist.items():
            total_score = sum(player.get_total_score())
            average_score = total_score / len(player.get_total_score())
            print(f"{name}: Total Score = {total_score}, Average Score = {average_score:.2f}")


class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, round_num, score):
        if len(self.scores) <= round_num:
            self.scores.append([])
        self.scores[round_num] = score

    def get_score(self, round_num):
        if round_num < len(self.scores):
            return self.scores[round_num]
        return '-'  # If the player has no score yet for this round

    def get_total_score(self):
        return [sum(round_scores) for round_scores in self.scores]


if __name__ == "__main__":
    shuffleboard_game = Shuffleboard()
    shuffleboard_game.loop_function()
    shuffleboard_game.play_game()
