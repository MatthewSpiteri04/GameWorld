from assets.colour_console import ColourConsole
import assets.validator as validate
from models.player import Player
from models.network import Network
from models.transfer import Request

cc = ColourConsole()
n = Network()

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
            in_menu = False
        else:
            cc.error_message("Invalid choice, please choose [1]!")
    cc.clear()
    choice = int(choice)
    if choice == 1:
        rock_paper_scissors(player)





def rock_paper_scissors(current_player : Player):
    n.connect()
    n.send_without_repsonse(Request("assign_player_to_game", "rock_paper_scissors", current_player))
    print("HI")



#main()
start_multiplayer(Player("Matthew"))
