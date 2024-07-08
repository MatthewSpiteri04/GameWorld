import socket
import pickle


class Network:
    def __init__(self):
        self.client = None
        self.server = "77.71.180.53"
        self.port = 5555
        self.addr = (self.server, self.port)

    def connect(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.addr)
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*4))
        except socket.error as e:
            print(e)

    def send_without_repsonse(self, data):
        try:
            self.client.send(pickle.dumps(data))
        except socket.error as e:
            print(e)

    def disconnect(self):
        try:
            self.client.close()
        except socket.error as e:
            print(e)