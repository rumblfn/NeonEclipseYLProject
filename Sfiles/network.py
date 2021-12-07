import socket
import pythonFB
import pickle
from time import sleep


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = pythonFB.getNetworkIpv4()
        self.port = pythonFB.getNetworkPort()
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def ch(self):
        self.p[0]['gameStatus'] = not self.p[0]['gameStatus']


while True:
    n = Network()
    print(n.p)
