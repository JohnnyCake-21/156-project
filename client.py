import socket


HEADER = 64 #header is the same
PORT = 6061 #ports have to match
SERVER = "192.168.56.1"  #client server is this
ADDR = (SERVER, PORT)
FORMAT = 'uft-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
