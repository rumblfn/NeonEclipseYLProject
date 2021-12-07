import socket
from _thread import start_new_thread
import pythonFB
import pickle
import sys


def getIpv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


server = getIpv4()
port = 5555
count_of_players = 0

pythonFB.setNetworkIpv4(server)
pythonFB.setNetworkPort(port)

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.bind((server, port))
socketServer.listen(2)
print('Waiting for a connection')


players = [{'gameStatus': False, 'count': 0}, {'gameStatus': False, 'count': 0}]


def threaded_client(conn, player):
    global count_of_players
    conn.send(pickle.dumps(players[player]))
    reply = ''
    replyStartGame = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            # if count_of_players == 2:
            #     replyStartGame = data.decode("utf-8")
            if not data:
                print('disconnected')
                break
            else:
                if player == 1:
                    reply = players[0]
                    reply['count'] = count_of_players
                else:
                    reply = players[1]
                    reply['count'] = count_of_players

                print("Received: ", data)
                print("Sending : ", reply)
            conn.sendall(pickle.dumps(reply))
            # con.sendall(str.encode(replyStartGame))
        except:
            break
    print('lost connection')
    count_of_players -= 1
    conn.close()


current_player = 0
while True:
    conn, addr = socketServer.accept()
    print('Connected to:', addr)
    count_of_players += 1
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1