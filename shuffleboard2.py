#text ChatGPT: create a shuffleboard class in python so i can play a game and keep the scores. I want to create names and keep the scores. Each time i enter a score i want to see the progress of the game in table layout with the names rounds and scores of the players. In the last row i want to see the total and avarage of each player. If a player enters an empty string the programm will stop or continue. If the stops it terminates the mainfunction and draws a final layout with underneath the winner of the game. Then keypress to exit to programm.

class ShuffleboardPlayer:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_total_score(self):
        return sum(self.scores)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0


class ShuffleboardGame:
    def __init__(self):
        self.players = []
        self.rounds = 1

    def add_player(self, name):
        player = ShuffleboardPlayer(name)
        self.players.append(player)

    def display_progress(self):
        table_header = ['Player']
        for i in range(1, self.rounds + 1):
            table_header.append(f'Round {i}')

        table_header.extend(['Total', 'Average'])
        print('\t'.join(table_header))

        for player in self.players:
            player_data = [player.name]
            player_data.extend(player.scores)
            player_data.extend([player.get_total_score(), player.get_average_score()])
            print('\t'.join(map(str, player_data)))

    def play_game(self):
        while True:
            self.display_progress()
            for player in self.players:
                score = input(f"{player.name}, enter your score for Round {self.rounds} (or hit Enter to stop): ")
                if not score:
                    quit_option = input(f"Do you want to quit, {player.name}? (Yes/No, default is Yes): ").lower()
                    if quit_option != 'no':
                        self.display_final_results()
                        return

                while not (score.isdigit() and 0 < int(score) <= 148):
                    print("Invalid score. Please enter a valid score (0 < score <= 148) or hit Enter to stop.")
                    score = input(f"{player.name}, enter your score for Round {self.rounds} (or hit Enter to stop): ")

                player.add_score(int(score))

            self.rounds += 1

    def display_final_results(self):
        self.display_progress()

        # Determine the winner
        winner = max(self.players, key=lambda player: player.get_total_score())
        print(f"\nWinner: {winner.name} with a total score of {winner.get_total_score()}")

        input("Press Enter to exit.")


if __name__ == "__main__":
    shuffleboard_game = ShuffleboardGame()
    while True:
        player_name = input("Enter player name (or hit Enter to start the game): ")
        if not player_name:
            break
        shuffleboard_game.add_player(player_name)

    shuffleboard_game.play_game()
