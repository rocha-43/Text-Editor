import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) 
FORMAT = 'utf-8'
DISCONET_MESSAGE = '!DISCONECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crirar um socket e fazer stream de daodos
server.bind(ADDR) #colocar o addr no socket

def handle_client(conn, addr):
  print(f'[NEW CONNECTION] {addr} CONNECTED.')
  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)  
    if msg_length:  # se msg_length tem algo
      msg_length = int(msg_length)                   
      msg = conn.recv(msg_length).decode(FORMAT)     
      if msg == DISCONET_MESSAGE:
        connected = False
      print(f'[{addr}] {msg}')
      conn.send("Msg received".encode(FORMAT))


def start():
  server.listen()
  print(f'[LISTENING] SERVER IS LISTENING ON {SERVER}')
  while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f'[ACTIVATE CONNECTIONS] {threading.activeCount() - 1}')

print('[STARTING] A INICIAR O SERVIDOR...')
start()


