import socket
from _thread import *
import pickle
from models.player_counts import PlayerCounts
from assets.colour_console import ColourConsole
from models.game_world import GameWorld
from models.transfer import Request, Response
from models.game import RockPaperScissors


server = "0.0.0.0"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cc = ColourConsole()

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
cc.server_says("Server Is Online!")
cc.server_says("Waiting for players...")

game_world = GameWorld()
player_counter = PlayerCounts()

def assign_to_game(game_world : GameWorld, request : Request ):
    game_id = -1
    if request.game == "rock_paper_scissors":
        player_counter.rock_paper_scissors_count += 1
        game_id = (player_counter.rock_paper_scissors_count - 1)//2
        if player_counter.rock_paper_scissors_count % 2 == 1:
            game_world.games[game_id] = RockPaperScissors(game_id, [request.player])
            cc.server_says(f"Generating 'Rock Paper Scissors' Game with Id {game_id}")
        else:
            game_world.games[game_id].players.append(request.player)
    return game_id

def threaded_client(conn, game_id):
    while True:
        try:
            request = pickle.loads(conn.recv(4096))

            if game_id in game_world.games:
                game = game_world.games[game_id]

                if not request:
                    break
                else:
                    conn.send(pickle.dumps(Response("Data")))


            else:
                break
        except:
            break
    print("Lost connection")
    try:
        if  game_id in game_world.games:
            del game_world.games[game_id]
            print("Closing Game", game_id)
    except:
        pass
    # THIS MUST CHANGE ACCORDING TO GAME
    player_counter.rock_paper_scissors_count -= 1
    conn.close()


while True:
    conn, addr = s.accept()

    request : Request = pickle.loads(conn.recv(4096))

    game_id = assign_to_game(game_world, request)

    start_new_thread(threaded_client, (conn, game_id))
