import sys
import os
from time import sleep
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONET_MESSAGE = '!DISCONECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
client.connect(ADDR)

class editor:
    def __init__(self, line, text):
        self.line = line
        self.text = text

    def write():
        """
        write the content in a file
        and render the interface
        """

        while True:
            line = ' $  '   # margem esquerda
            open_file = input('[OPEN FILE] [Y, n]   $ ') # set do arquivo
            print('\n')
        
            if open_file == 'Y':
                file_name = input('[FILE NAME]   $ ')
                print('\n')
                try:
                    arq = open(file_name, 'w')   # recebe o arquivo
                except:
                    print('[ERROR] FILE NOT FOUND')
                    print('\n')
            elif open_file == 'n':
                delete_file = input('[DELETE FILE] [Y, n]  $ \n')  # set apagar
                if delete_file == 'Y':
                    try:
                        delete_name = input('[FILE NAME]   $ ')
                        os.remove(delete_name)   # apagar
                    except:
                        print('[FILE NOT FOUND]')
                        pass
                elif delete_file == 'n':
                    print('[IN 5 SEC. I WILL CLOSE] THANK YOU FOR USING!')
                    sleep(5)
                    sys.exit()  # sair

            while True: # escrever   
                text = str(input("""  $ """))
                arq.write(text + '\n')



u = editor 
u.write()


