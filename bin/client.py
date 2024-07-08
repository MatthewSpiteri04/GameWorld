from assets.colour_console import ColourConsole
import assets.validator as validate
from models.player import Player, RockPaperScissorsPlayer
from models.network import Network
from models.transfer import Request, Response
from models.game import Game, RockPaperScissors

cc = ColourConsole()
n = Network()

def get_other_player_name(id, players):
    for p in players:
        p : Player 
        if id != p.id:
            return p.name

def main():
    # Initialisation
    cc.print_space("Greetings!")
    cc.print_space("Welcome")
    cc.print_new_line("to my Game World!")
    cc.line()
    your_player = Player(cc.get_input("What's your name: "))
    cc.line()
    cc.print_space("Welcome,")
    cc.print_new_line(your_player.name + "!", cc.red)
    cc.print_space("Press")
    cc.print_space("[Enter]", cc.yellow)
    cc.get_input("To Proceed...")
    cc.clear()

    in_menu = True
    
    # Show Menu
    while in_menu:
        cc.print_title("Choose Game Type")
        cc.print_new_line("1. Single-Player")
        cc.print_new_line("2. Multiplayer")
        cc.line()
        cc.small_pause()
        choice = cc.get_input("Your choice: ")
        if validate.main_menu(choice) is True:
            in_menu = False
        else:
            cc.error_message("Invalid choice, please choose between [1] or [2]!")
    cc.clear()
    if choice == 1:
        start_single_player(your_player)
    elif choice == 2:
        start_multiplayer(your_player)


def start_single_player(player : Player):
    pass


def start_multiplayer(player : Player):
    in_menu = True
    while in_menu:
        cc.print_title("Choose Game To Play!")
        cc.print_new_line("1. Rock, Paper, Scissors")
        cc.line()
        cc.small_pause()
        choice = cc.get_input("Your choice: ")
        if validate.multiplayer_menu(choice) is True:
            cc.clear()
            choice = int(choice)
            if choice == 1:
                rock_paper_scissors(player)
        else:
            cc.error_message("Invalid choice, please choose [1]!")
    


def rock_paper_scissors(current_player : Player):
    game_active = True
    n.connect()
    n.send_without_repsonse(Request("assign_player_to_game", "rock_paper_scissors", current_player))
    cc.print_new_line("Connection established, Waiting for another player to join...", time=0)
    while game_active:
        try:
            response : Response = n.send(Request("get_game", "rock_paper_scissors", current_player))
        except:
            game_active = False
            cc.error_message("Couldn't get game")
        game : RockPaperScissors = response.data    
        if len(game.players) == 2:
            break

    cc.clear()
    cc.print_title("Rock Paper Scissors")
    cc.line()
    cc.print_space(current_player.name, cc.yellow)
    cc.print_space("vs")
    cc.print_new_line(get_other_player_name(current_player.id, game.players), cc.yellow)
    cc.line()

    while (game.player1.score < 2) and (game.player2.score < 2):
        index = 0
        cc.print_title("Pick A Move")
        for option in game.choices:
            index += 1
            cc.print_new_line(f"{index}. {option}", time=0.05)
        cc.small_pause()
        choice = cc.get_input("Your choice: ")
        if validate.rps(choice) is True:
            
            if game.player1.id == current_player.id:
                game.player1.ready = True
                game.player1.choice = int(choice)
                n.send_without_repsonse(Request("update_game_player", "rock_paper_scissors", game.player1, 1))
            elif game.player2.id == current_player.id:
                game.player2.ready = True
                game.player2.choice = int(choice)
                n.send_without_repsonse(Request("update_game_player", "rock_paper_scissors", game.player2, 2))

            while True:
                try:
                    response : Response = n.send(Request("get_game", "rock_paper_scissors", current_player))
                except:
                    cc.error_message("Error Ocurred")
                    break
                game : RockPaperScissors = response.data    
                if game.player2.ready and game.player1.ready:
                    break
            
            winner = game.determine_winner()
            game.player1.ready = False
            game.player2.ready = False
            if winner is not None and winner.id == current_player.id:
                cc.print_new_line(winner.name + " Wins!", cc.green)
            elif winner is not None and winner.id != current_player.id:
                cc.print_new_line(winner.name + " Wins!", cc.red)
            else:
                cc.print_new_line("It's a Draw!")

            response : Response = n.send(Request("update_game", "rock_paper_scissors", game))
            game = response.data

        else:
            cc.error_message("Invalid choice, please choose [1], [2] or [3]!")

    cc.print_new_line("Game Over", cc.cyan)
    n.disconnect()

main()
