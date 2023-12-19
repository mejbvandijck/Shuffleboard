#An errorneos programm made by ChatGPT
#input: write a python programm that keeps the score of the game shuffleboard. In this programm i want a class with the name Shuffleboard. I also want a loopfunction to create player objects with ascending numbers like: player1, player2 and so on. The players objects have a name and a score.  The name will be asked for when creating the object. The score will be set to self.score = [].  There must also be a variable playerslist in the Shuffleboard class, where each player(key) and each name(value) will be stored as dictionary item. This loopfunction will repeat until the user hit an empty string. This means the loopfunction stops. round1 starts. The programm draws a layout from a def layout_shuffleboard(round) function. round keeps track on how many rows will be printed. The minimum rows to print is 2. The first row starts with an empty cell then followed by all names from all players. The following row should start with the word: round and his according number. this will be round1 for the first round. round2 for the second round. The rest of the row will be printed accordingly to the name of the player with his score.  If the player has no score yet there must appear an -. After the layout_shuffleboard(round) function there will be printed a text wich player needs to enter his score: f"{playerslist[value]} enter your score: ".  The player will enter his score, but this score needs to be a valid score like 0<score<=148. then the score will be stored in his player object as self.score wich is a list. If its not a valid score or an empty string, the player will be asked again to enter his score until its a valid score or an empty string. The first round is the first score. Each other round the scores will be added to the according players self.score. If this player leaves an empty string, he gets the option to quit the game with ' Yes'  as default option. This means if this value is an empty string he wants to quit.  The programm will print the layout with the final results. Here the avarage scores and total scores will be added in the layout. There will be printed a last line with the text: " Thank you for using this programm." Then with a keypress the programm will terminate (exit).  If The player entered a valid score the programm keeps continuing. The layout will appear again, but this time its player2 turn. Then player2 will enter his score. Like the first player if its a valid score, the game continues like before. This process will repeat untill all players have had there turn. After that round2 will start and the layout will be adjusted accordingly.  If the game quits the programm will show the layout again, but this time the total score and avarages per player will be added.

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
