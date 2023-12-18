# laatste aangepaste versie (speelbaar)

class ShuffleboardPlayer:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_total_score(self):
        return sum(self.scores)

    def get_average_score(self):
        return round(sum(self.scores) / len(self.scores)) if self.scores else 0


class ShuffleboardGame:
    def __init__(self):
        self.players = []
        self.rounds = 1

    def add_player(self, name):
        player = ShuffleboardPlayer(name)
        self.players.append(player)

    def display_progress(self):
        table_header = ['Spelers']
        for i in range(1, self.rounds):
            table_header.append(f'Ronde {i}')

        table_header.extend(['Totaal', 'Gemiddeld'])
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
                score = input(f"{player.name}, wat is jouw score voor ronde {self.rounds} (druk op Enter om te stoppen): ")
                if not score:
                    quit_option = input(f"Wil je stoppen, {player.name}? (druk een toets om naar de uitslag te gaan, wil je dit niet? toets: 'Nee'): ").lower()
                    if quit_option != 'nee':
                        self.display_final_results()
                        return

                while not (score.isdigit() and 0 < int(score) <= 148):
                    print("Foute score! Vul een score in tussen 0 en 148 of druk op Enter om te stoppen.")
                    score = input(f"{player.name}, vul de score in van ronde {self.rounds} (druk op Enter om te stoppen): ")

                player.add_score(int(score))

            self.rounds += 1

    def display_final_results(self):
        self.display_progress()

        # Determine the winner
        winner = max(self.players, key=lambda player: player.get_total_score())
        print(f"\nWinnaar: {winner.name} met een totale score van {winner.get_total_score()} en een gemiddelde van {winner.get_average_score()}")

        input("Druk op een toets om af te sluiten")


if __name__ == "__main__":
    shuffleboard_game = ShuffleboardGame()
    while True:
        player_name = input("Naam nieuwe speler:  (druk op Enter om geen nieuwe spelers meer toe te voegen): ").title()
        if not player_name:
            break
        shuffleboard_game.add_player(player_name)

    shuffleboard_game.play_game()